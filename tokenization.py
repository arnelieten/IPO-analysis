import nltk
nltk.download('punkt')
import os
import nltk
from nltk.tokenize import word_tokenize

def tokenize_text_file(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens

def save_tokens_to_file(tokens, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for token in tokens:
            file.write(token + '\n')

def process_text_files_in_folder(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            
            # Tokenize the text in the file
            tokens = tokenize_text_file(input_file_path)
            
            # Save the tokenized text to a new file
            save_tokens_to_file(tokens, output_file_path)

# Specify the folders
input_folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Text Files'
output_folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Tokenized Files'

# Process all text files in the folder
process_text_files_in_folder(input_folder_path, output_folder_path)

print("Tokenization completed.")
