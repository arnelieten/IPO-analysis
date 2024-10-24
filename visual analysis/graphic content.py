import os
import fitz  # PyMuPDF
import csv

def count_inline_images_in_pdf_content_stream(doc):
    """Count inline images represented by "BI" in PDF content streams."""
    inline_image_count = 0
    for page in doc:
        page_text = page.get_text("text")
        inline_image_count += page_text.count("BI")
    return inline_image_count

def count_unique_images_in_pdf(pdf_path):
    """Count unique images by referencing their xref and counting inline images in PDF."""
    doc = fitz.open(pdf_path)
    unique_images = set()

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        for image_info in image_list:
            img_xref = image_info[0]
            unique_images.add(img_xref)

    inline_image_count = count_inline_images_in_pdf_content_stream(doc)
    doc.close()
    return len(unique_images), inline_image_count

def iterate_pdf_folder_and_count_images(folder_path, output_csv_file):
    """Iterate through PDFs in a folder, count images, and output results to CSV."""
    results = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            isin_number = os.path.splitext(filename)[0]  # Extract ISIN number from filename without extension
            pdf_path = os.path.join(folder_path, filename)
            xobject_images, inline_images = count_unique_images_in_pdf(pdf_path)
            results.append({
                'ISIN': isin_number,
                'XObject Images': xobject_images,
                'Inline Images': inline_images
            })
            print(f"File: {filename} - XObject Images: {xobject_images}, Inline Images: {inline_images}")

    # Write the results to a CSV file
    with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['ISIN', 'XObject Images', 'Inline Images'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)

# Define your folder path and CSV file path
folder_path = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Prospectus PDFs'
output_csv_file = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Features\Graphic content analysis\graphic content.csv'

# Call the function
iterate_pdf_folder_and_count_images(folder_path, output_csv_file)
print('Graphic content determined')


