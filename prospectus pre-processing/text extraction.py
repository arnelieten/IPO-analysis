import os
import fitz

def extract_text_from_pdf(pdf_path, output_path):
    """
    Extracts text from a PDF file using PyMuPDF and writes it to a text file.

    :param pdf_path: Path to the PDF file.
    :param output_path: Path to save the extracted text file.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Ensure the output path has the correct .txt extension
    output_path = os.path.splitext(output_path)[0] + '.txt'

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Text successfully extracted and saved to {output_path}")

def process_all_pdfs(input_folder, output_folder):
    """
    Processes all PDF files in the specified folder, extracting text and saving it as text files.

    :param input_folder: Folder containing PDF files.
    :param output_folder: Folder where extracted text files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each PDF in the directory
    for filename in os.listdir(input_folder):
        # Handle case insensitivity by checking the lower case of filename
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            # Ensure output filename ends with .txt
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_path = os.path.join(output_folder, output_filename)
            print(f"Processing {pdf_path}...")
            extract_text_from_pdf(pdf_path, output_path)

# Specify the directory containing your PDFs and where to save the output text files
input_folder = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus PDFs'
output_folder = r'C:\\Users\\arnel\\OneDrive - KU Leuven\\Thesis Economics\\Python\\Prospectus Text Files'

# Process all PDFs in the specified folder
process_all_pdfs(input_folder, output_folder)

### Save PDF files as txt files in directory!!


