import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\JMP\Tables\data (day).csv')

# Select variables
print(df.columns.tolist())
df = df[['ISIN', 'UpRevision (%)', 'Share Overhang (%)', 'Log[Shares Offered]', 'Log[Proceeds Amount (€)]', 'Log[Word count]', 'Log[Page count]', 'Log[Inline Images+1]', 'Log[Total Images+1]', "Yule's I", 'Subjectivity (ML)', 'Polarity (ML)', 'Negative share (ML)', 'Positive share (ML)', 'Negative share (D)', 'Positive share (D)']]
df = df.sort_values(by='ISIN', key=lambda x: x.str[:2], ascending=True)
df = df.head(110)
df = df.drop(columns='ISIN')

# Calculate Pearson correlation matrix
correlation_matrix = df.corr(method='pearson')


# Plot correlation matrix as a heatmap
plt.figure(figsize=(8,8))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt='.2f')
plt.title('Pearson Correlation Matrix of Quantitative Input Variables', fontsize=15, pad=25)
plt.show()
