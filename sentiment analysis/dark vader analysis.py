import os
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# Directory containing the text files
input_directory = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Processed Files English'
# Directory where the CSV will be saved
output_directory = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\Sentiment analysis'
output_file = os.path.join(output_directory, 'vader_analysis.csv')

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List to hold the data
data = []

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Process each file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        # Remove the .txt suffix from the filename
        isin = os.path.splitext(filename)[0]
        file_path = os.path.join(input_directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Get VADER scores
            scores = sia.polarity_scores(text)
            # Append the results along with the file name
            data.append([isin, scores['neg'], scores['neu'], scores['pos'], scores['compound']])

# Create a DataFrame
df = pd.DataFrame(data, columns=['ISIN', 'Negative', 'Neutral', 'Positive', 'Compound'])

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)

print(f"Dark Vader Analysis completed")
