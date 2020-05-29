# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here

#Data Checks
data.head()
data.info()
data.columns

#Reading column 'Gender' and replace '-' with 'Agender'

#Checking the values in Gender column
data['Gender'].unique()
#Replacing the values
data['Gender'].replace('-','Agender', inplace=True)
#Checking the values in Gender column to see if they are replaced
data['Gender'].unique()
#Checking the distribution of Gender by ploting a graph with proper labels
data['Gender'].value_counts(ascending=True).plot(kind='barh', title='Gender Distribution amongst the Superheroes')

#Does good overpower evil or does evil overwhelm good?
#Checking the distribution of 'Alignment' column
data['Alignment'].value_counts()
#Checking the distribution of Alignment by ploting a graph with proper labels
data['Alignment'].value_counts(ascending=True).plot(kind='barh', title='Alignment Distribution amongst the Superheroes')

#For any of the members, combat skills are really important to survive when they find themselves in unwanted situtations. Check out if combat relate to person's strength or it's intelligence?
#Function to get Pearson's Correlation Coefficient
def pearson_corr(data1, data2):
    covariance = data1.cov(data2)
    std_data1 = data1.std()
    std_data2 = data2.std()
    
    return (covariance/(std_data1*std_data2))    

#Checking for correlation between 'Combat' and 'Strength' using Pearsons method
pearson_corr(data['Combat'], data['Strength'])
#Checking for correlation between 'Combat' and 'Intelligence' using Pearsons method
pearson_corr(data['Combat'], data['Intelligence'])

#Find out who are the best of the best in this superhero universe?
#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)
#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]
#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])
#Printing the names
print(super_best_names)


