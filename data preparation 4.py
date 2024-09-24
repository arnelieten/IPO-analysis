### Link Global Orbis database with Zephyr database ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load both databases
df_global = pd.read_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Data\prepared data 3.csv', parse_dates=['IPO date'])
df_zephyr = pd.read_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Data\accounting data zephyr.csv')

# Drop Unnamed: 0 & Deal value (th)
df_zephyr=df_zephyr.drop(columns='Unnamed: 0')
df_zephyr=df_zephyr.drop(columns='Deal value\nth EUR')

# Rename columns (Company, ISIN number, Ticker symbol, Underwriter, Offer price, Closing price (day), Closing price (week), Closing price (month))
df_zephyr.rename(columns={'Target name': 'Company','Target ISIN number': 'ISIN number',
                          'Target ticker symbol':'Ticker symbol','Advisors name': 'Underwriter',
                          'Target stock price at completion date\nEUR':'Offer price',
                          'Target stock price after completion\nEUR': 'Closing price (day)',
                          'Target stock price 1 week after completion\nEUR':'Closing price (week)',
                          'Target stock price 1 month after completion\nEUR': 'Closing price (month)',}, inplace=True)

# Convert Deal value, Offer price, Closing price (day),Closing price (week),Closing price (month) to numeric data type
df_zephyr['Offer price'] = pd.to_numeric(df_zephyr['Offer price'], errors='coerce')
df_zephyr['Closing price (day)'] = pd.to_numeric(df_zephyr['Closing price (day)'], errors='coerce')
df_zephyr['Closing price (week)'] = pd.to_numeric(df_zephyr['Closing price (week)'], errors='coerce')
df_zephyr['Closing price (month)'] = pd.to_numeric(df_zephyr['Closing price (month)'], errors='coerce')

# Merge both dataframes
merged_df = pd.merge(df_global, df_zephyr, on='ISIN number', how='left', suffixes=('', '_zephyr'))
df = merged_df.drop_duplicates()

# Remove Company_zephyr, Ticker symbol_zephyr and Deal type
df=df.drop(columns='Company_zephyr')
df=df.drop(columns='Deal type')
df=df.drop(columns='Ticker symbol_zephyr')

# Count nan values for the rows
nan_counts_row = []

for index, row in df.iterrows():
    nan_count = row.isna().sum()
    nan_counts_row.append((index, nan_count))

nan_counts_df = pd.DataFrame(nan_counts_row, columns=['Row Index', 'NaN Count'])

# Plot the occurence of the values of the nan values in a row  
nan_count_occurrences = nan_counts_df['NaN Count'].value_counts()
plt.figure(figsize=(10, 6))
nan_count_occurrences.plot(kind='bar')
plt.title('Occurrences of NaN Counts')
plt.xlabel('Number of NaNs in a Row')
plt.ylabel('Occurrences')
plt.xticks(rotation=0)
plt.show()

# Keep the rows with 0 or 1 nan values CHECK GB COMPANIES IN REFINITIV!!!!
#nan_counts_per_row = df.isna().sum(axis=1)
#df = df[(nan_counts_per_row == 0) | (nan_counts_per_row == 1)]

# Check balance of dataset
category_counts = df['Country'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette="viridis")
plt.xlabel('Category', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Count of Categorical Values', fontsize=16)
plt.xticks(rotation=90, fontsize=12) 
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# Export csv files
df.to_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Data\prepared data 4.csv', index=False)
df.to_csv(r'C:\Users\arnel\thesis\CSV FILES\prepared data 4.csv', index=False)
print('prepared data 4 = ready')