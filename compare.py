import fitz  # PyMuPDF
import os

def compare(og_cleaned_folder, new_cleaned_folder):

    # Get the list of PDF files in both folders
    og_pdf_files = os.listdir(og_cleaned_folder)
    new_pdf_files = os.listdir(new_cleaned_folder)

    # Sort the file lists to ensure sequential comparison
    og_pdf_files.sort()
    new_pdf_files.sort()

    # Iterate through the PDF files and compare them
    for og_pdf_file, new_pdf_file in zip(og_pdf_files, new_pdf_files):
        og_pdf_path = os.path.join(og_cleaned_folder, og_pdf_file)
        new_pdf_path = os.path.join(new_cleaned_folder, new_pdf_file)

        # Open the PDF files using PyMuPDF
        og_pdf_document = fitz.open(og_pdf_path)
        new_pdf_document = fitz.open(new_pdf_path)

        # Get the number of pages in each PDF
        og_num_pages = len(og_pdf_document)
        new_num_pages = len(new_pdf_document)

        # Get the number of words in each PDF
        og_num_words = sum(len(page.get_text("text")) for page in og_pdf_document)
        new_num_words = sum(len(page.get_text("text")) for page in new_pdf_document)

        # Get the number of images in each PDF (assuming images are counted as XObjects)
        og_num_images = sum(len(page.get_images(full=True)) for page in og_pdf_document)
        new_num_images = sum(len(page.get_images(full=True)) for page in new_pdf_document)

        # Close the PDF documents
        og_pdf_document.close()
        new_pdf_document.close()

        # Compare the extracted information
        if og_num_pages != new_num_pages or og_num_words != new_num_words or og_num_images != new_num_images:
            print(f"Differences found in {og_pdf_file} and {new_pdf_file}.")
            return (0)

    # If the loop completes without any differences, print a success message
    print("No differences found in the two folders.")
    return (1)
