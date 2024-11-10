#importing data
import pandas as pd
data1 = pd.read_excel("C:/Users/Admin/OneDrive/Документы/Documents/OneDrive/Documents/DSA/CustomerMaster.xlsx")
data2 = pd.read_csv("C:/Users/Admin/OneDrive/Документы/Documents/OneDrive/Documents/DSA/Bankloan.csv")

print(data1)
print(data2)
print(data1.columns)

#selecting columns
selected_data = data1[['CustomerGroup', 'CityProvince']]
print(selected_data)

#filtering Rows
filtered_data = data2[data2['age'] > 50]

#Adding new columns
data1['age_sets'] = data1[('CustomerGroup')] * 2

#Grouping and aggregation
# grouped_data = data1.groupby('CustomerGroup').agg({'CityProvince': 'mean', ''})

#sorting data
sorted_data = data1.sort_values(by='CustomerGroup', ascending=False)
print(sorted_data)

#removing missing values
data_cleaned = data1.dropna()
print(data_cleaned)

#Performing descriptive analytics techniques
#Data visualization
#histogram for numeric data
import matplotlib.pyplot as plt
data2['age'].hist(bins=20)
plt.title('Histogram of Employees')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#bar plot for categorical data
data1['CustomerGroup'].value_counts().plot(kind='bar')
plt.title('Bar Plot of categorical Column')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.show()

#clustered Graph (e.g., scatter plot for clusters
import seaborn as sns
sns.scatterplot(data=data1, x='CustomerGroup', y='CityProvince', hue='PrimaryContact')
plt.title('Clustered Scatter Plot')
plt.show()

#summary statistics
summary = data2.describe()
print(summary)

#frequency table
#frequency table with intervals
data1['binned_column'] = pd.cut(data2['age'], bins=[0, 10, 20, 30, 40, 50])
print(data1['binned_column'].value_counts())

#frequency table without intervals
print(data2['age'].value_counts())

#cross tabulation
crosstab = pd.crosstab(data1['CustomerGroup'], data1['CityProvince'])
print(crosstab)
