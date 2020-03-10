# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
df = pd.read_csv(path,delimiter=';')

# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
# replace the unknown words with nan
df = df.replace('unknown', np.nan)

# check the null values
print(df.isnull().sum())

# dropna
df.dropna(inplace=True)

# check the null values
print(df.isnull().sum())

# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
df.rename(columns={'loan': 'previous_loan_status', 'y': 'loan_status'}, inplace=True)
print(df.head())

# Find out the information of the `job` column.
# How many different variants of job are there?
print(df['job'].nunique())

#Total different types of job
print(df['job'].unique())

# Counts for different types of `job`
print(df['job'].value_counts())


# Check the `loan_status`  approval rate by `job`
df.groupby('job').loan_status.value_counts(normalize = True)

# Check the percentage of loan approved by `education`
df[df['loan_status'] == 'yes']['education'].value_counts(normalize=True)

# Check the percentage of loan approved by `previous loan status`
df[df['loan_status'] == 'yes']['previous_loan_status'].value_counts(normalize=True)

# Create a pivot table between `loan_status` and `marital ` with values form `age`
pivot = df.pivot_table(index='loan_status', values='age', columns='marital')
print(pivot)

# Loan status based on marital status whose status is married
loan_stat=df[df['marital'].apply(lambda marital: marital == 'married')]
marital_status_summery= loan_stat['loan_status'].value_counts()
print (marital_status_summery)

#Create a  Dataframes 

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
# class 1
branch_1 = {
        'customer_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Andrew', 'Alex', 'Sabestian', 'Hilary', 'Jack'], 
        'last_name': ['Ng', 'Hales', 'Rachaska', 'Masan', 'Anthony']}
df_branch_1 = pd.DataFrame(branch_1, columns = ['customer_id', 'first_name', 'last_name'])
print(df_branch_1)

# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
# class 2
branch_2 = {
        'customer_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Brain', 'Steve', 'Kim', 'Steve', 'Ben'], 
        'last_name': ['Alexander', 'Jobs', 'Jonas', 'Fleming', 'Richardsan']}
df_branch_2 = pd.DataFrame(branch_2, columns = ['customer_id', 'first_name', 'last_name'])
print(df_branch_2)
# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value
# test_score
credit_score = {
        'customer_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'score': [513, 675, 165, 961, 1080, 1654, 415, 900, 610, 1116]}
df_credit_score = pd.DataFrame(credit_score, columns = ['customer_id','score'])
print(df_credit_score)

# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new = pd.concat([df_branch_1, df_branch_2])
print(df_new)

# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
pd.merge(df_new, df_credit_score, left_on='customer_id', right_on='customer_id')


