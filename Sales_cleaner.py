import pandas as pd
file_path = 'Online Sales Retailer.xlsx'
df_sales = pd.read_excel(file_path, sheet_name='Sales', engine='openpyxl')
df_Product = pd.read_excel(file_path, sheet_name='Product', engine='openpyxl')
df_Invoice = pd.read_excel(file_path, sheet_name='Invoice', engine='openpyxl')
print(df_sales.head())
print(df_Product.head())
print(df_Invoice.head())
df_rows = len(df_sales) + len(df_Product) + len(df_Invoice)
print(f"Total number of rows across all sheets: {df_rows}")
# Creating a total sales column in the df_sales Dataframe 
df_sales['total_sales'] = df_sales['Quantity'] * df_sales['UnitPrice']
print(df_sales.head())
# Merging the three DataFrames on the 'product_id' and 'invoice_id' columns
df_merged = pd.merge(df_sales, df_Invoice, on='InvoiceNo', how='left')
df_final = pd.merge(df_merged, df_Product, on='StockCode', how='left')
print(df_final.head())
#Filtering the total_sales column by changing the missing values to zero and the unit_price column by changing the missing values to zero
df_final['total_sales'] = df_final['total_sales'].fillna(0)
df_final['UnitPrice'] = df_final['UnitPrice'].fillna(0)
total_values_missing = df_final['total_sales'].isnull().sum()
print(f"Total number of missing values in the 'total_sales' column: {total_values_missing}")
# now I am gonna group the Stockcode with the total_sales column and sum the totalal_sales column and sort the values in ascending order 
df_grouped = df_final.groupby('StockCode')['total_sales'].sum().reset_index().sort_values(by='total_sales', ascending=False)
print(df_grouped.head(10))
# I need to import matplpotlib and seaborn to visualise the data 
import matplotlib.pylab as plt 
import seaborn as sns 
# setting the theme to be white 
sns.set_theme(style="whitegrid")
# creating the size of the figure 
plt.figure(figsize=(12, 6))
# creating a bar plot to visualise the relationship between the stockcode and the total_sales column 
sns.barplot(data=df_grouped.head(10), x='StockCode', y='total_sales', hue='StockCode', palette='viridis', legend=False)
plt.title('Top Products by Total Sales')
plt.xlabel('Stock Code')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

