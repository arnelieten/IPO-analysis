import pandas as pd
import numpy as np
import re
import os
import datetime as dt
import sys

# Define a class to handle dictionary words and sentiment categories
class MasterDictionary:
    def __init__(self, cols, stopwords):
        for ptr, col in enumerate(cols):
            if col == '':
                cols[ptr] = '0'
        self.word = cols[0].upper()
        self.negative = int(cols[7])
        self.positive = int(cols[8])
        self.uncertainty = int(cols[9])
        self.stopword = self.word in stopwords

# Load the sentiment dictionary
def load_masterdictionary(file_path, stopwords):
    _master_dictionary = {}
    with open(file_path, 'r') as f:
        next(f)  # skip header
        for line in f:
            cols = line.strip().split(',')
            word = cols[0]
            _master_dictionary[word] = MasterDictionary(cols, stopwords)
    return _master_dictionary

# Read the text file
def read_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text

# Tokenize the text
def tokenize(text):
    return re.findall(r'\b\w+\b', text)

# Count sentiments
def count_sentiments(words, dictionary):
    sentiments = {'Positive Dictionary': 0, 'Negative Dictionary': 0, 'Uncertainty Dictionary': 0}
    for word in words:
        if word.upper() in dictionary and not dictionary[word.upper()].stopword:
            if dictionary[word.upper()].positive:
                sentiments['Positive Dictionary'] += 1
            if dictionary[word.upper()].negative:
                sentiments['Negative Dictionary'] += 1
            if dictionary[word.upper()].uncertainty:
                sentiments['Uncertainty Dictionary'] += 1
    return sentiments

# Process each file in a folder
def process_folder(folder_path, dictionary):
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            text = read_text(file_path)
            words = tokenize(text)
            sentiment_counts = count_sentiments(words, dictionary)
            # Remove the .txt suffix from filename before saving to the results
            sentiment_counts['ISIN'] = filename[:-4]  # Remove last 4 characters (.txt)
            results.append(sentiment_counts)
    
    # Specify the path directly in the to_csv method to avoid confusion and ensure it is clear
    results_df = pd.DataFrame(results)
    results_df.to_csv(r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\Sentiment analysis\dictionary_analysis.csv', index=False)


# Main execution
if __name__ == '__main__':
    dictionary_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\Sentiment analysis\Dictionary.csv'
    folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Processed Files English'
    stopwords = set(['A', 'THE', 'AND', 'BUT', 'IT', 'OR', 'AS', 'OF', 'AT', 'BY', 'FOR', 'WITH', 'ABOUT', 'AGAINST', 'BETWEEN', 'INTO', 'THROUGH', 'DURING', 'BEFORE', 'AFTER'])
    master_dictionary = load_masterdictionary(dictionary_path, stopwords)
    process_folder(folder_path, master_dictionary)

print('dictionary analysis completed')

