import os
import re
import regex

def preprocess_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        processed_text = file.read()
    
    # Remove URL, HTML, and www links
    processed_text = re.sub(r'http[s]?://\S+', '', processed_text)
    processed_text = re.sub(r'www\.\S+', '', processed_text)
    processed_text = re.sub(r'<a href=.*?>.*?</a>', '', processed_text)

    # Remove numbers
    processed_text = re.sub(r'.?\d+.?', ' ', processed_text)

    # Remove abbreviations
    processed_text = re.sub(r'\b(?:[A-Z]\.)+[A-Z]?\b', '', processed_text)
    processed_text = re.sub(r'\b(?:[a-z]\.)+[a-z]?\b', '', processed_text)
    processed_text = re.sub(r'\b[A-Z]\.\b', '', processed_text)
    processed_text = re.sub(r'\b[a-z]\.\b', '', processed_text)
    processed_text = re.sub(r'\b[a-z]{2,}\.\b', '', processed_text)
    processed_text = re.sub(r'\b(?:[A-Z]{1,2}\.)+[A-Z]?|e\.g\.|i\.e\.|etc\.|vs\.|\b\w{2,3}\.\b|U\.S\.|U\.K\.|E\.U\.|N\.Y\.|sec\.|min\.|hr\.|kg\.|cm\.|mm\.|mi\.|viz\.|ibid\.|op\. cit\.|loc\. cit\.', '', processed_text)

    # Remove all hyphens and dashes, including en and em dashes
    processed_text = re.sub(r'[-–—]', '', processed_text)

    # Remove brackets with less than 4 characters inside (round, square, curly)
    processed_text = re.sub(r'\([^\)]{1,4}\)', '', processed_text)
    processed_text = re.sub(r'\[[^\]]{1,4}\]', '', processed_text)
    processed_text = re.sub(r'\{[^\}]{1,4}\}', '', processed_text)

    # Remove all mathematical symbols
    processed_text = re.sub(r'[\+\-=×÷√]', '', processed_text)

    # Remove all sorts of brackets
    processed_text = re.sub(r'\([^)]*\)', '', processed_text)
    processed_text = re.sub(r'\[[^\]]*\]', '', processed_text)
    processed_text = re.sub(r'\{[^}]*\}', '', processed_text)

    # Remove unpaired unpaired brackets
    processed_text = regex.sub(r'\((?=\s|\Z)', '', processed_text)
    processed_text = regex.sub(r'(?<=\s|\A)\)', '', processed_text)

    # Remove miscellaneous symbols
    processed_text = re.sub(r'[&@#%+§*~<>^|]', '', processed_text)

    # Remove punctuation (not period, not exclamation mark, not question mark)
    processed_text = re.sub(r'[^\w\s\.\!\?]', '', processed_text)

    # Remove sequences of periods to remove content tables
    processed_text = re.sub(r'\.{2,}', '.', processed_text)

    # Remove single letters
    processed_text = re.sub(r'\b[a-zA-Z]\b', '', processed_text)

    # Remove all whitespace before periods
    processed_text = re.sub(r'\s+\.', '.', processed_text)

    # Normalize multiple spaces to a single space
    processed_text = re.sub(r'\s+', ' ', processed_text)

    # Convert all text to lowercase
    processed_text = processed_text.lower()

    # Remove sequences of two or more periods with a single period
    processed_text = re.sub(r'\.{2,}', '.', processed_text)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(processed_text)

def process_all_files(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename.replace(" Processed.txt", ".txt"))
            print(f"Processing {input_path}...")
            preprocess_file(input_path, output_path)
            print(f"Processed and saved to {output_path}")

# Specify the input directory containing your text files
input_directory = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Text Files'

# Specify the output directory for storing processed text files
output_directory = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Processed Files'

# Process all text files in the specified directory
process_all_files(input_directory, output_directory)

print('Text processed')
