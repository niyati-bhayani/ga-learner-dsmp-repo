# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank_data = pd.read_csv(path)

#Code starts here

"""Step 1: Let's check which variable is categorical and which one is numerical so that       you will get a basic idea about the features of the bank dataset"""

bank = pd.read_csv(path)

# To check which variable is a categorical variabe
categorical_var = bank.select_dtypes(include = 'object')
print("Categorical Features are: \n", categorical_var.columns)

# To check which variable is a numerical variabe
numerical_var = bank.select_dtypes(include = 'number')
print("Numerical Features are: \n", numerical_var.columns)

""" Step 2: Sometimes customers forget to fill in all the details or they don't want to share other details. Because of that, some of the fields in the dataset will have missing values. Now you have to check which columns have missing values and also check the count of missing values each column has. If you get the columns that have missing values, try to fill them."""

# Drop 'Loan_ID' column
banks = bank.drop(['Loan_ID'], axis = 1)
banks.head()

# To check the count of null values in each column
print(banks.isnull().sum())

# To calculate the mode for each column
bank_mode = banks.mode()
print(bank_mode)

# To fill the NaN values in each column with respective modes
for colname in banks.columns:
    banks[colname].fillna(bank_mode[colname].iloc[0], inplace = True)

# To check the count of null values in each column
print(banks.isnull().sum())

# To display the first 5 rows of the dataset
banks.head()

""" Step 3: Now let's check the loan amount of an average person based on 'Gender', 'Married', 'Self_Employed'. This will give a basic idea of the average loan amount of a person."""

avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc = 'mean')
print(avg_loan_amount)

"""Step 4: Now let's check the percentage of loan approved based on a person's employment type."""

loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]['Loan_Status'].value_counts()
print("Count of Self-Employed people who got the loan approved: ", loan_approved_se[0])

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]['Loan_Status'].value_counts()
print("Count of Non Self-Employed people who got the loan approved: ", loan_approved_nse[0])

loan_status_count = banks['Loan_Status'].value_counts().sum()

percentage_se = round((loan_approved_se[0]/loan_status_count)*100, 2)
print("The percentage of loan approval for self-employed people: ", percentage_se)

percentage_nse = round((loan_approved_nse[0]/loan_status_count)*100, 2)
print("The percentage of loan approval for non self-employed people: ", percentage_nse)

"""Step 5: A government audit is happening real soon! So the company wants to find out those applicants with long loan amount term."""

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
big_loan_term = len(loan_term[loan_term>=25])
print("Number of applicants with loan amount term greater than or equal to 25: ", big_loan_term)

""" Step 6: Now let's check the average income of an applicant and the average loan given to a person based on their income."""

loan_groupby = banks.groupby(by = ['Loan_Status'])

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
loan_groupby.head()

mean_values = loan_groupby.mean()
print("Average Income of the applicants whose loan got approved: ", round(mean_values.iloc[1,0],2))








