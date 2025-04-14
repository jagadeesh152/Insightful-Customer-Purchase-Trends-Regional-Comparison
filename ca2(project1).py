import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
a=pd.read_excel("C:\\Users\\jagad\\Documents\\Downloads\\customer_data.xlsx")

print(a)
print(a.head())
print(a.tail())
print(a.info()) #details
print(a.describe()) #deatil of the dataset mean and std min etc
print(a.columns)
print(a.isnull().sum())


# 1

#Compare total and average purchase amounts by region (e.g., Asia vs North America).
# Group by region and calculate the total and average purchase amount
region_summary = a.groupby('Region')['Purchase Amount'].agg(  #dataframe group by
    total_purchase='sum',
    average_purchase='mean'
)   #.reset_index()
# # Display the results
print(region_summary)


# Plotting the barplot for average purchase by region
plt.figure(figsize=(10, 6))
sns.barplot(data=region_summary, x='Region', y='total_purchase', palette='viridis')
plt.title('Total Purchase Amount by Region')
plt.xlabel('Region')
plt.ylabel('Total Purchase Amount')
##plt.xticks(rotation=0)
plt.show()


2
# List the top 10 customers based on their purchase amount.

top_10_customers = a.sort_values(by='Purchase Amount', ascending=False).head(10)
print("Top 10 Customers Based on Purchase Amount:")
print(top_10_customers[['Name', 'Email', 'Purchase Amount']])

# Plotting the lineplot for average purchase by region
plt.figure(figsize=(10, 6))
sns.lineplot(x=top_10_customers.index, y='Purchase Amount', data=top_10_customers, marker='o')
plt.title('Purchase Amounts of Top 10 Customers (Line Plot)')
plt.xlabel('Customer Index')
plt.ylabel('Purchase Amount')
plt.show()


# 3
# Find the Most Common Customer Names Analyze which names appear most frequently

name_counts = a['Name'].value_counts()
print("Most Common Customer Names:")
print(name_counts)

# Plotting the scatterplot  Most Common Customer Names
plt.figure(figsize=(10, 6))
sns.scatterplot(x=name_counts.head(10).index, y=name_counts.head(10).values, color='purple')
plt.title('Frequency of Top 10 Customer Names (Scatter Plot)')
plt.xlabel('Customer Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# 4
#4 location wise region compasion of puschase amount
print(a.columns)
a.columns = a.columns.str.strip()
a = a.dropna(subset=['Purchase Amount', 'Region'])
a['Purchase Amount'] = pd.to_numeric(a['Purchase Amount'], errors='coerce')
region_stats = a.groupby('Region')['Purchase Amount'].agg(['sum', 'mean', 'count']).reset_index()
print(region_stats)

#  Pie Chart: Share of Total Purchase by Region
plt.figure(figsize=(6,6))
plt.pie(region_stats['sum'], labels=region_stats['Region'], autopct='%1.1f%%', startangle=140)
plt.title('Region-wise Share of Total Purchase')
plt.tight_layout()
plt.show()

 # 5
# analyze Region wise puschase amount
a.columns = a.columns.str.strip()
print("Columns:", a.columns)
a = a.dropna(subset=['Purchase Amount', 'Region'])
a['Purchase Amount'] = pd.to_numeric(a['Purchase Amount'], errors='coerce')
a = a.dropna(subset=['Purchase Amount'])
region_analysis = a.groupby('Region')['Purchase Amount'].agg(
    Total_Purchase='sum',
    Average_Purchase='mean',
    Number_of_Customers='count'
).reset_index()
print(region_analysis)
plt.figure(figsize=(10, 6))
sns.histplot(data=a, x='Purchase Amount', hue='Region', bins=20, kde=True, multiple='stack')
plt.title('Purchase Amount Distribution by Region')
plt.xlabel('Purchase Amount')
plt.ylabel('Number of Customers')
plt.show()


q1=df['Values'].quantile(0.25)
print(q1)
q3=df['Values'].quantile(0.75)
print(q3)
iqr=q3-q1
print(iqr)
lower_bound=q1-1.5*iqr
print(lower_bound)
upper_bound=q3+1.5*iqr
print(upper_bound)
outlier=df[(df['Values']<lower_bound)|(df['Values']>upper_bound)]
print(outlier)