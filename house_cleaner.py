import io 
import pandas as pd 
from azure.storage.blob import BlobServiceClient
connection_string = "DefaultEndpointsProtocol=https;AccountName=level5data;AccountKey=cWgxWhPELQdrW0sIgA/eXM8/k9+xdaELukN8sg5imfhm4wVIJQFmypEph/Ppy500v41mYT+iCBbC+AStsfHbAQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = "businesscases"
blob_name = "house_sales_prediction.csv"
# Download the blob data into a bytes object
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
stream = io.BytesIO(blob_client.download_blob().readall())
df_house_cleaner = pd.read_csv(stream)
print(df_house_cleaner.head()) 
df_house_cleaner.info()
import matplotlib.pyplot as plt 
import seaborn as sns 
# discriptive summery statistics 
print(df_house_cleaner.describe())
# setting the theme to be white 
sns.set_theme(style="whitegrid")

# Task 2.2: visualise the relationship between square feet and price using scatter plot 
fig, axes = plt.subplots(1, 3, figsize=(15, 6))
sns.scatterplot(data=df_house_cleaner, x='Square_Feet', y='Price', ax=axes[0], alpha=0.7)
axes[0].set_title('Square Feet vs Price')
axes[0].set_xlabel('Square Feet')
axes[0].set_ylabel('Price')


#Task 2.3: visualising the distribution of the Price using a histogram
sns.histplot(data=df_house_cleaner, x='Price', bins=20, kde=True, ax=axes[1], edgecolor='black')
axes[1].set_title('Distribution of Price')
axes[1].set_xlabel('Price')
axes[1].set_ylabel('Frequency')

#Task 2.4: Computing and visualizing the correlation matrix between the features
correlation_matrix = df_house_cleaner.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt='.2f', linewidths=0.5, ax=axes[2])
axes[2].set_title('Correlation Matrix')
plt.tight_layout()
plt.show()