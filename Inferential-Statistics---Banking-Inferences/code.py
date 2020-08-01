# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

#Task1 - Confidence Interval
#Sampling the dataframe
data_sample = data.sample(n=sample_size, random_state=0)


#Finding the mean of the sample
sample_mean = data_sample['installment'].mean()

#Finding the standard deviation of the sample
sample_std = data_sample['installment'].std()

#Finding the margin of error
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))

#Finding the confidence interval
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval:")
print(confidence_interval)

#Finding the true mean
true_mean=data['installment'].mean()

print(("True mean: {}".format(true_mean)))

#Task2 - CLT
#Create an array of three different sample sizes: 20,50,100
sample_size_array = np.array([20, 50, 100])
#Creating different subplots
fig, axes = plt.subplots(3, 1, figsize=(10,20));

#Running loop to iterate through rows
for i in range(len(sample_size_array)):
    
    #Initiating a list for means
    m = []
    
    #Loop to implement the number of samples
    for j in range(1000):
        
        #Finding mean of a random sample
        mean = data['installment'].sample(n=sample_size_array[i]).mean()
        
        #Appending the mean to the list
        m.append(mean)
    
    #Converting the list to series
    mean_series = pd.Series(m)
    
    
    #Plotting the histogram for the series
    axes[i].hist(mean_series)

#Displaying the plot
plt.show()

#Task 3 - Small Business Interests
from statsmodels.stats.weightstats import ztest

#Interest rate for small businesses and converting the column from % to float values
x1 = data[data['purpose']=='small_business']['int.rate'].str[:-1].astype(float)

#Apply ztest with value as mean of the interest rate column
z_statistic_1, p_value_1 = ztest(x1, value=data['int.rate'].str[:-1].astype(float).mean(), alternative='larger')

#Print z statistic and p value
print("Z-statistics = ",z_statistic_1)
print("p-value = ",p_value_1)

#Check the p-value
if p_value_1<0.05:
    inference='Reject: Interest rate being given to people with purpose as small_business is higher than the average interest rate'
else:
    inference='Failed to Reject: There is no difference in interest rate being given to people with purpose as small_business'
print("Inference:", inference)

#Task 4 - Installment vs Loan Defaulting
#Applying ztest for the hypothesis
z_statistic_2, p_value_2 = ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])

print(('Z-statistic 2 is :{}'.format(z_statistic_2)))
print(('P-value 2 is :{}'.format(p_value_2)))

#Check the p-value
if p_value_2<0.05:
    inference='Reject: There is a difference in installments being paid by loan defaulters and loan non-defaulters'
else:
    inference='Failed to Reject: There is no difference in installments being paid by loan defaulters and loan non-defaulters'
print("Inference:", inference)

#Task 5 - Purpose vs Loan Defaulting
#Find out the value counts of different purposes when customers have paid back loan and when they haven't and store them all
purpose_yes_counts = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
purpose_no_counts = data[data['paid.back.loan']=='No']['purpose'].value_counts()

#Concatenating the above two dataframes into a single dataframe
observed = pd.concat([purpose_yes_counts.transpose(), purpose_no_counts.transpose()], axis = 1, keys=['Yes', 'No'])

#Find out the chi2 value of the above stored values
chi2, p, dof, ex = chi2_contingency(observed)

#Inference
if chi2>critical_value:
    inference='Reject: There is a difference in the distribution of purpose for loan defaulters and non defaulters'
else:
    inference='Failed to Reject: There is no difference the distribution of purpose for loan defaulters and non defaulters'
print("Inference:", inference)


