print("Hello, World")
#string functions with the just the names
#  
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Michael")

# Example numbers to divide
numbers = [18, 0, 'a', 9]

for number in numbers:
    try:
        # Try to divide 18 by the number
        result = 18 / number
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        # This will run if the number is zero (division by zero)
        print("Error: You can't divide by zero.")
    except TypeError:
        # This will run if the number is not a valid type (e.g., string instead of int)
        print(f"Error: '{number}' is not a valid number for division.")

        my_dictionary = {"name": "John", "age": 30, "work": "Engineer", "time": "Morning"}
        print(my_dictionary["name"])

import pandas as pd
data = {
    'employee_id': range(1, 21),
    'name': ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack', 'Karen', 'Leo', 'Mia', 'Nina', 'Olivia', 'Paul', 'Quinn', 'Rita'],
    'age': [22, 25, 28, 35, 40, 42, 50, 60, 65, 30, 28, 24, 37, 41, 48, 33, 29, 32, 45, 38],
    'department': ['HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales'],
    'salary': [50000, 60000, 55000, 75000, 80000, 85000, 100000, 110000, 120000, 65000, 67000, 72000, 85000, 90000, 95000, 48000, 67000, 70000, 80000, 88000],
    'work_experience': [1, 3, 5, 7, 10, 12, 15, 18, 20, 3, 1, 6, 4, 8, 5, 7, 3, 2, 6, 5],
}
df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())

print(df.describe())

df['years_to_retirement'] = 65 - df['age'] 
df.rename(columns={'salary': 'annual_salary'}, inplace=True)
df = df.sort_values(by='work_experience')
print(df)

df = df.sort_values(by='work_experience', ascending=False)
print(df)
df['increase total sales'] = df['annual_salary'].apply(lambda x: x * 1.10)
#seeing the values that are missing in the data frame 
missing_values = df.isnull().any(axis=1)
df = df[~missing_values]
#replacing the missing values with a zero 
df.fillna(0, inplace=True)
#cleaning my data by taking out the null values 
df.dropna(inplace=True)
#creating null values in the dateframe 
df.loc[5, 'annual_salary'] = None
df.loc[4, 'annual_salary'] = None
df.loc[3, 'annual_salary'] = None
df.loc[4, 'age'] = None
df.loc[3, 'age'] = None
df.loc[2, 'age'] = None
df_mean= df[['annual_salary', 'age']].mean()
df[['annual_salary', 'age']] = df[['annual_salary', 'age']].fillna(df_mean)
#finding out the employees who are older than 30 names, ages, departments, and salaries
older_than_30 = df[df['age'] > 30][['name', 'age', 'department', 'annual_salary']]
print(older_than_30)
# finding out the mean, mode and count of the ages of the employees in the data frame
df_age_stats = df['age'].agg(['mean', 'mode', 'count'])
print(df_age_stats)
