import pandas as pd 
file_path = 'my.pythonwork/cdYMhMv8Qy2uv3RKsAve_SalesData (1).xlsx'
df_sales = pd.read_excel(file_path, sheet_name='Sales', engine='openpyxl')
df_Products = pd.read_excel(file_path, sheet_name='Product', engine='openpyxl')
df_Date = pd.read_excel(file_path, sheet_name='Date', engine='openpyxl')
df_Store = pd.read_excel(file_path, sheet_name='Store', engine='openpyxl')
print(df_sales.head())
print(df_Products.head())
print(df_Date.head())
print(df_Store.head())
df_rows = len(df_sales) + len(df_Products) + len(df_Date) + len(df_Store)
print(f"Total number of rows across all sheets: {df_rows}")
# merge sales and products on 'ProductCode'
df_merged = pd.merge(df_sales, df_Products, on='ProductCode', how='left')
# merge the result with the Store
df_final = pd.merge(df_merged, df_Store, on='StoreCode', how='left')
# merge the result with the Date
df_final = pd.merge(df_final, df_Date, on='Date', how='left')
print(df_final.head())
total_rows = len(df_final)
print(f"Total number of rows in the final merged DataFrame: {total_rows}")
#looking for missing values in the final merged DataFrame
print(df_final.isnull().sum())
#creating a new column by dividing the 'sales' column by the 'quantity' column to get the unit price
df_final['unit_price'] = df_final['Sales'] / df_final['Quantity']
df_final.rename(columns={'Sales': 'total_sales'}, inplace=True)
print(df_final.head())
#the mean, mode, median and std of Quataty and mean of Sales 
mean_total_sales = df_final['total_sales'].mean()
median_total_sales = df_final['total_sales'].median()
mode_total_sales = df_final['total_sales'].mode()
std_total_sales = df_final['total_sales'].std()
mean_quantity = df_final['Quantity'].mean()
median_quantity = df_final['Quantity'].median()
mode_quantity = df_final['Quantity'].mode()
std_quantity = df_final['Quantity'].std()
print(f"Mean of Sales: {mean_total_sales}")
print(f"Median of Sales: {median_total_sales}")
print(f"Mode of Sales: {mode_total_sales[0] if not mode_total_sales.empty else 'No mode found'}")
print(f"Std of Sales: {std_total_sales}")
print(f"Mean of Quantity: {mean_quantity}")
print(f"Median of Quantity: {median_quantity}")
print(f"Mode of Quantity: {mode_quantity[0] if not mode_quantity.empty else 'No mode found'}")
print(f"Std of Quantity: {std_quantity}")
# changing the date into a datetime format 
df_final['Date'] = pd.to_datetime(df_final['Date'])
# grouping the datetime by the total_sales 
df_grouped = df_final.groupby(df_final['Date'].dt.to_period('M'))['total_sales'].sum().reset_index()
print(df_grouped)
df_grouped['Date'] = df_grouped['Date'].astype(str)
# creating a line plot to visualise the relationship between the date and the total_sales column
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_grouped, x='Date', y='total_sales', marker='o', color='blue')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Group the data by Quarterly and sum the total_sales 
df_final['Quarterly'] = pd.to_datetime(df_final['Date']).dt.to_period('Q').astype(str)
df_quarterly_sales = df_final.groupby('Quarterly')['total_sales'].sum().reset_index()
#sort by sales and take the top 5 quarterly sales 
df_quarterly_sales = df_quarterly_sales.sort_values('total_sales', ascending=False).head(5)
plt.figure(figsize=(12, 8))
plt.pie(df_quarterly_sales['total_sales'], labels=df_quarterly_sales['Quarterly'].astype(str), 
autopct='%1.1f%%', startangle=90, colors=plt.cm.Set3.colors[:len(df_quarterly_sales)])
plt.title('Total sales distribution by Quarter')
plt.ylabel('')
plt.tight_layout()
plt.show()

# correlation between the total_sale and the quantity column 
correlation = df_final[['total_sales', 'Quantity']].corr()
print(f"correlation between total_sales and Quantity: {correlation.loc['total_sales', 'Quantity']}")

# Creating a heatmap of the correlation between the total_sales and the quantity column
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Correlation between Total Sales and Quantity')
plt.xlabel('Total Sales')
plt.ylabel('Quantity')
plt.show()
# creating a pivot table that contains the total_sales, StoreCode and month_year 
pivot_table = df_final.pivot_table(values='total_sales', index='StoreCode', columns='Quarterly', aggfunc='sum')
pivot_table = pivot_table.reset_index()
print(pivot_table)

# creating a bar plot by using the pivot_table to visualise the relationship between the StoreCode and the total_sales in each quarter
plt.figure(figsize=(12, 6))
sns.barplot(data=pivot_table.melt(id_vars='StoreCode', var_name='Quarterly', value_name='total_sales'),
 x='StoreCode', y='total_sales', hue='Quarterly', palette='viridis')
plt.title('Total Sales by Store and Quarter')
plt.xlabel('Store Code')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Quarterly')
plt.tight_layout()
plt.show()