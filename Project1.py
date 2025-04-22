import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_excel("C:/Users/Parth/Downloads/Sales Records (2).xlsx")


# Calculate Profit
df['Profit'] = df['Total Revenue'] - df['Total Cost']

# Set plot style
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Bar Chart - Total Units Sold by Item Type
plt.figure()
df.groupby('Item Type')['Units Sold'].sum().sort_values().plot(kind='barh', color='skyblue')
plt.title('Total Units Sold by Item Type')
plt.xlabel('Units Sold')
plt.ylabel('Item Type')
plt.tight_layout()

# 2. Pie Chart - Total Revenue by Country (top 5 countries)
plt.figure()
top_countries = df.groupby('Country')['Total Revenue'].sum().sort_values(ascending=False).head(5)
top_countries.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Top 5 Countries by Total Revenue')
plt.ylabel('')
plt.tight_layout()

# 3. Histogram - Distribution of Unit Prices
plt.figure()
sns.histplot(df['Unit Price'], bins=20, kde=True, color='orange')
plt.title('Distribution of Unit Prices')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.tight_layout()


plt.figure()
sns.boxplot(data=df, x='Region', y='Profit')
plt.xticks(rotation=90)
plt.title('Profit Distribution by Region')
plt.ylabel('Profit')
plt.xlabel('Region')
plt.tight_layout()

# 5. Heatmap - Correlation Matrix
plt.figure()
numeric_cols = ['Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Profit']
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()

plt.show()


# INT 375 Data Visualization Project This Showssales report of Region, country , product sales...and statical analysis
# Signature- A Chakravarty, 12319336, Lovely prof.  university

