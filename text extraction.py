import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    
    for page in doc:
        text += page.get_text()
        
    doc.close()
    return text

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)

def process_pdfs_in_folder(folder_path, output_folder):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(pdf_path)
            
            # Generate the output text file path
            base_name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_folder, f"{base_name}.txt")
            
            # Save the extracted text
            save_text_to_file(text, output_path)

# Specify the folder containing the PDFs and the folder where you want to save the text files
input_folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus PDFs'
output_folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus Text Files'

# Ensure the output folder exists
os.makedirs(output_folder_path, exist_ok=True)

# Process all PDFs in the folder
process_pdfs_in_folder(input_folder_path, output_folder_path)

print("Text extraction from PDFs completed.")