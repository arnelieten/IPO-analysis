import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load csv file
df = pd.read_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Data\Prepared data.csv', parse_dates=['IPO Date'])

# Extract year from 'IPO_date' and create a new column
df['IPO_year'] = df['IPO Date'].dt.year

# Count the number of IPOs per year
ipo_year_counts = df['IPO_year'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=ipo_year_counts.index, y=ipo_year_counts.values, palette="viridis")
plt.xlabel('', fontsize=14)
plt.ylabel('Number of IPOs', fontsize=14)
plt.title('IPO Date Segmentation', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()