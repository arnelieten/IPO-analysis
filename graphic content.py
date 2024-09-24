import os
import fitz  # PyMuPDF
import pandas as pd

def count_images_in_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    image_count = 0
    
    for page in doc:
        image_list = page.get_images(full=True)
        image_count += len(image_list)
    doc.close()
    return image_count

def analyze_pdfs_in_folder(folder_path):
    data = {"Title": [], "Image Count": []}
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            image_count = count_images_in_pdf(pdf_path)
            data["Title"].append(os.path.splitext(filename)[0])  # Removing the .pdf extension
            data["Image Count"].append(image_count)
    
    return pd.DataFrame(data)

# Specify the folder containing the PDFs
folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus PDFs'
df = analyze_pdfs_in_folder(folder_path)

# Specify the new path to save the CSV file
csv_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\graphic content.csv'
df.to_csv(csv_path, index=False)

print("Figures counting completed.")