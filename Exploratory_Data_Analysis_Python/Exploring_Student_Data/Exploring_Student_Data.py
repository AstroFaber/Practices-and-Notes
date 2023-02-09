# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('students.csv')

# Print first few rows of data
print(students.head())

# Print summary statistics for all columns
print(students.describe(include='all'))
print("")

# Calculate mean
print('Mean: {0}'.format(students.math_grade.mean()))

# Calculate median
print('Median: {0}'.format(students.math_grade.median()))

# Calculate mode
print('Mode: {0}'.format(students.math_grade.mode()[0]))

# Calculate range
print('Range: {0}'.format(students.math_grade.max() - students.math_grade.min()))

# Calculate standard deviation
print('Standard Deviation: {0}'.format(students.math_grade.std()))

# Calculate MAD
print('MAD: {0}'.format(students.math_grade.mad()))
print("")

#create an histogram for math grades

sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
Mjob = students.Mjob.value_counts()
print("Number of students with mothers in each job category:")
print(Mjob)
print("")

# Calculate proportion of students with mothers in each job category
Mjob_prop = students.Mjob.value_counts() / len(students.Mjob)
print(Mjob_prop)

# Create bar chart of Mjob
sns.countplot(students.Mjob)
plt.show()
plt.clf()

# Create pie chart of Mjob

students.Mjob.value_counts().plot.pie()
plt.axis('equal')
plt.show()