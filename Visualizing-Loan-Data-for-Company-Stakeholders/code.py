# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here
"""Step 1: Let's start with the simple task of visualizing the company's record with respect to loan approvals.
"""
# Step 1 
#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind='bar', title='Status of Loan Approval', rot = 0, color = 'green')

"""Insight: The count of loans approved is 50% higher than the count of loans not approved
Food for Thought: Can one of the company's health factors be its loan status distribution?
"""

# Step 2

""" Step 2: The company provides financial assistance across the different regions of the country. One interesting statistic that stakeholders want to see is the loan approval distribution across the regions.
"""

#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack().plot(kind='bar', stacked=False, title = 'Loan Approval Status in Different Areas')

#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

"""Insight: 1) Semiurban area has Highest number of Loan Approvals; while the Rural area has the Lowest number of Loan Approvals
2) Semiurban area has the Maximum Difference between Loan Approvals and Loan Rejections
"""

# Step 3
"""Step 3:Higher education has always been an expensive endeavour for people but it results in better career opportunities and stability in life. But does higher education result in a better guarantee in issuing loans?
"""

#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = education_and_loan.size().unstack().plot(kind='bar', stacked=True, title = 'Education vs Loan Approval Status')

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)

"""Insights: 1) Overall Graduates have asked for higher loan services as compared to Non-Graduates, irrespective of the Approval.
2) Graduates have better approval to non-approval ratio as compared to Non-Graduates.
Food for thought: Is higher education an expensive endeavor? or Does higher education result in a better guarantee in issuing loans?
"""

# Step 4 
"""Step 4: After seeing the loan status distribution, let's check whether being graduate or not also leads to different loan amount distribution by plotting an overlapping density plot of two values.
"""
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate'].fillna(0)

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate'].fillna(0)

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')

#Plotting density plot for 'Not Graduate'
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')

#For automatic legend display
plt.legend()

"""Insights: 1) The average amount of loan approved for the graduates and the non graduates is the same.
"""

# Step 5
"""Step 5: For any financial institution to be successful in its loan lending system, there has to be a correlation between the borrower's income and loan amount he is lent. Let's see how our company fares in that respect. 
"""
#Setting up the subplots
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows=3, ncols=1, figsize=(15,15))
fig.tight_layout(pad=10.0) #To create space between the subplots to make it look neater

#Plotting scatter plot
data.plot.scatter(x='ApplicantIncome', y='LoanAmount', ax=ax_1)

#Setting the subplot axis title
ax_1.set_title('Applicant Income')

#Plotting scatter plot
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount', ax=ax_2)

#Setting the subplot axis title
ax_2.set_title('Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome'] 

#Plotting scatter plot
data.plot.scatter(x='TotalIncome', y='LoanAmount', ax=ax_3)

#Setting the subplot axis title
ax_3.set_title('Total Income')

"""Insights: There is a correlation between Applicant Income and Loan Amount. 
However, there is a stronger correlation between Total Income and Loan Amount.
"""


