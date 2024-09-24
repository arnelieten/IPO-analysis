import os
import csv

# Specify the directory containing the text files
directory_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Text Files'

# Specify the CSV file path where the results will be saved
csv_file_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\word count.csv'

# Function to count words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
        words = contents.split()
        return len(words)

# Create or overwrite the CSV file and write headers
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File Name', 'Word Count'])

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            # Full path to the text file
            full_path = os.path.join(directory_path, filename)
            
            # Count words in the text file
            word_count = count_words_in_file(full_path)
            
            # Write the file name and word count to the CSV
            writer.writerow([filename, word_count])

print('Word counts have been written to', csv_file_path)
