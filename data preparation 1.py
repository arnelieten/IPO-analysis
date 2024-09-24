import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Data\accounting data.csv')

# Rename columns to (Company & Industry)
df.rename(columns={'Company name Latin alphabet': 'Company','BvD sectors': 'Industry','Country ISO code':'Country'}, inplace=True)

# Filter European exchanges (London Stock Exchange, Borsa Italiana, Nasdaq OMX, Euronext Paris, Warsaw Stock Exchangem,...)
exchanges_to_remove = ["Nordic Growth Market (NGM)", "Boerse Munchen", "New York Stock Exchange (NYSE)",
    "Bern Stock Exchange", "Bolsa de Madrid", "Nasdaq OMX - Tallinn", "Zagreb Stock Exchange",
    "Banja Luka Stock Exchange", "Sarajevo Stock Exchange", "Nasdaq OMX - Iceland",
    "Athens Stock Exchange", "Euronext Lisbon", "Norvegian OTC", "The International Stock Exchange",
    "Euronext Dublin", "Australian Securities Exchange", "OTC Bulletin Board", "Nasdaq OMX - Riga",
    "Bolsa de Barcelona", "Hong Kong Stock Exchange", "Boerse Hamburg", "Boerse Stuttgart",
    "NASDAQ Capital Market", "TSX Venture Exchange", "Euronext Access Paris", "Nasdaq OMX - Vilnius",
    "Malta Stock Exchange", "Cyprus Stock Exchange", "Perspectiva Stock Exchange", "Moscow Exchange MICEX - RTS",
    "NASDAQ National Market", "Istanbul Stock Exchange", "London Stock Exchange (SEAQ)"]

df= df[~df['Main exchange'].isin(exchanges_to_remove)]

# Filter countries with lower than 5 IPOs
country_counts = df['Country'].value_counts()
countries_to_remove = country_counts[country_counts <= 5].index.tolist()
df= df[~df['Country'].isin(countries_to_remove)]

# Filter industry groups with lower than 5 IPOs
country_counts = df['Industry'].value_counts()
countries_to_remove = country_counts[country_counts <= 5].index.tolist()
df= df[~df['Industry'].isin(countries_to_remove)]

# Convert IPO date to datetime64
df['IPO date'] = pd.to_datetime(df['IPO date'], format='%d/%m/%Y')

# Drop nan values in columns (Company name, IPO date, ISIN number, )
df = df.dropna(subset=['IPO date'])
df = df.dropna(subset=['Company'])
df = df.dropna(subset=['ISIN number'])
df = df.dropna(subset=['Industry'])
df = df.dropna(subset=['Ticker symbol'])
df = df.dropna(subset=['Main exchange'])
df = df.dropna(subset=['Currency'])

# Plot count of 'Country' in a bar chart
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

# Reset index & remove anomalous quantitative data
df.drop('Unnamed: 0', axis=1, inplace=True)
df.reset_index(inplace=True)
df.drop('index', axis=1, inplace=True)
df = df.replace({'n.a.': np.nan, 'n.s.': np.nan})

# Export to csv
df.to_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Data\prepared data 1.csv', index=False)
df.to_csv(r'C:\Users\arnel\thesis\CSV FILES\prepared data 1.csv', index=False)
print('prepared data 1 = ready')
