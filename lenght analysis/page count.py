import os
import fitz  # Import PyMuPDF
import csv

# Specify the directory containing the PDF files
directory_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus PDFs'

# Specify the CSV file path where the results will be saved
csv_file_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\Length analysis\page counts.csv'

# Function to count pages in a PDF file
def count_pages_in_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        return len(doc)

# Create or overwrite the CSV file and write headers
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ISIN', 'Page count'])

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            # Full path to the PDF file
            full_path = os.path.join(directory_path, filename)
            
            # Count pages in the PDF file
            page_count = count_pages_in_pdf(full_path)
            
            # Get the filename without its extension for the ISIN number
            isin_number = os.path.splitext(filename)[0]
            
            # Write the ISIN number (filename without extension) and page count to the CSV
            writer.writerow([isin_number, page_count])

print('Pages have been counted')

