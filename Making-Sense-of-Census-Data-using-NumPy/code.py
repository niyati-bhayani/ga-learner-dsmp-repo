# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

# Reading file
# The path to the data set has been stored in the variable named path.
# Load the dataset and store it in a variable called data using np.genfromtxt()
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
""" Step 1: In this first task, we will load the data to a numpy array and add a new record to it."""
census = np.concatenate((data, new_record), axis=0)

# Checking the shape of both the datasets to see if the new record has been added
print("Shape of 'data' array: ", data.shape)
print("Shape of 'census' array: ", census.shape)

""" Step 2: We often associate the potential of a country based on the age distribution 
of the people residing there. We too want to do a simple analysis of the age          distribution."""

age = census[:,0]
max_age = np.max(age)
print("Maximum age of the population is: ", max_age)
min_age = np.min(age)
print("Minimum age of the population is: ", min_age)
age_mean = np.mean(age)
print("Mean age of the population is: ", age_mean)
age_std = np.std(age)
print("Standard Deviation of the population age is: ", age_std)

""" Step 3: The constitution of the country tries it's best to ensure that people of all races are able to live harmoniously. Let's check the country's race distribution to identify the minorities so that the government can help them."""

race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

length_list = [len_0, len_1, len_2, len_3, len_4]
minority_race = length_list.index(min(length_list))
print('Race with minimum number of citizens is:', minority_race)

""" Step 4: As per the new govt. policy, all citizens above age 60 should not be 
made to work more than 25 hours per week. Let us look at the data and see if that policy is followed."""

senior_citizens = census[census[:,0]>60]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len

if avg_working_hours > 25:
    print("Average Working Hours = " +str(round(avg_working_hours,2)) + " hours per week\nThis means that the government policy is not followed")
else:
    print("Average Working Hours = " +str(round(avg_working_hours,2)) + " hours per week\nThis means that the government policy is followed")

""" Step 5: Our parents have repeatedly told us that we need to study well in order 
to get a good(read: higher-paying) job. Let's see whether the higher educated people 
have better pay in general."""

high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

if avg_pay_high > avg_pay_low:
    print("Better education leads to better pay as " +str(round(avg_pay_high,2)*100)+ "% educated people have an annual income of more than 50K")
    print("\nAmongst less educated people "+str(round(avg_pay_low,2)*100)+ "% people have an annual income of more than 50K")
   
else:
    print("Better education does not lead to better pay")

#Code ends here


