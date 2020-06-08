# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

#Read the first 5 lines
df.head()

#Get info on dataset
df.info()

#Get shape of dataframe
df.shape

#To check whether the condition 'fico' credit score is greater than 700 and purpose == 'debt_consolidation' is independent 
#of each other

#Probability of fico credit scored greather than 700
p_a = len(df[df['fico']>700])/df.shape[0]

#Probability of purpose being 'Debt Consolidation'
p_b = len(df[df['purpose']=='debt_consolidation'])/df.shape[0]

#Probability of both the events happening together
p_a_b = len(df[(df['fico']>700) & (df['purpose']=='debt_consolidation')])/df.shape[0]

#Are events a and b independent?
result = (p_a*p_b==p_a_b)
print("Are events a and b independent?", result)

#Calculating conditional probability is a very important step.
#Let's calculate the Bayes theorem for the probability of credit policy is yes and the person is given the loan.

#Calulate the proportion of users that has Paid Back Loan --> P(A)
new_df = df[df['paid.back.loan']=='Yes']
prob_lp = new_df.shape[0]/df.shape[0]
print("Probability of users that has Paid Back Loan:", prob_lp)

#Calulate the proportion of users that meets the credit underwriting criteria of LendingClub.com --> P(B)
prob_cs = df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print("Probability of users that meets the credit underwriting criteria of LendingClub.com:", prob_cs)

#Calculate conditional probability of users that meet credit underwriting criteria given that they have Paid Back Loan -- P(B|A)
prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print("Probability of users that meet credit underwriting criteria given that they have Paid Back Loan:", prob_pd_cs)

#Calculate conditional probability of users that has Paid Back Loan given that they meet credit underwriting criteria -- P(A|B)
bayes = round((prob_pd_cs*prob_lp)/prob_cs, 4)
print("Probability of users that has Paid Back Loan given that they meet credit underwriting criteria:", bayes)

#Purpose for defaulting on the loan

#Study the values in purpose column
print('The values in purpose column are:', df['purpose'].unique())

#Calculate the paid.back.loan == No and the store the result in dataframe df1
df1 = df[df['paid.back.loan']=='No']
print('Shape of new dataframe:', df1.shape)
df1['purpose'].value_counts(ascending=True).plot(kind='barh', title='Purpose for  Defaulting on Loans')

#Let's plot the histogram for visualization of the continuous variable - 'Installment'

#Calculate the median for installment and store it in variable inst_median
inst_median = df['installment'].median()

#Calculate the mean for installment and store it in variable inst_mean
inst_mean = df['installment'].mean()

#Calculate the mode for installment and store it in variable inst_mode
inst_mode = df['installment'].mode()

#Plot the histogram for installment
plt.hist(df['installment'], bins=40)
plt.axvline(inst_mean, label='mean', color='k', linestyle='dashed', linewidth=1)
plt.axvline(inst_median, label='median', color='r', linestyle='dashed', linewidth=1)
#plt.axvline(inst_mode, label='mode', color='k', linestyle='dashed', linewidth=1)
plt.legend()

#Let's plot the histogram for visualization of the continuous variable - 'Log Annual Income'

#Calculate the median
lac_median = df['log.annual.inc'].median()

#Calculate the mean
lac_mean = df['log.annual.inc'].mean()

#Calculate the mode
lac_mode = df['log.annual.inc'].mode()

#Plot the histogram for Log Annual Income
plt.hist(df['log.annual.inc'], bins=40)
plt.axvline(lac_mean, label='mean', color='k', linestyle='dashed', linewidth=1)
plt.axvline(lac_median, label='median', color='r', linestyle='dashed', linewidth=1)
#plt.axvline(inst_mode, label='mode', color='k', linestyle='dashed', linewidth=1)
plt.legend()







