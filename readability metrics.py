import os
import csv
import textstat

def extract_readability_metrics(folder_path):
    # Define the CSV file name where the results will be saved
    csv_file_name = 'readability_metrics.csv'
    
    # Open the CSV file for writing
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['File Name', 'Flesch Kincaid Grade', 'Gunning Fog Index'])
        
        # Iterate over all the text files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                # Construct full file path
                file_path = os.path.join(folder_path, filename)
                # Read the text file
                with open(file_path, 'r', encoding='utf-8') as text_file:
                    text = text_file.read()
                    # Calculate Flesch Kincaid Grade
                    fk_grade = textstat.flesch_kincaid_grade(text)
                    # Calculate Gunning Fog Index
                    gunning_fog = textstat.gunning_fog(text)
                    # Write the metrics to the CSV file
                    writer.writerow([filename, fk_grade, gunning_fog])
    print(f'Results saved to {csv_file_name}')

# Example usage
folder_path = 'path/to/your/text/files'
extract_readability_metrics(folder_path)
