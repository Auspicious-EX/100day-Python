# DAY 76 : Exercise 8 - Merge the PDF

""" 
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
 """

import os
from PyPDF2 import PdfWriter, PdfReader

def merge_pdfs(directory_path):
    output_pdf = "merged_output.pdf"
    pdf_writer = PdfWriter()

    # Check if the directory path exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    # Iterate over files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(directory_path, filename)
            print(f"Merging {filename}...")
            pdf_reader = PdfReader(filepath)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_pdf, "wb") as output_file:
        pdf_writer.write(output_file)

    print(f"PDF files in '{directory_path}' merged successfully to '{output_pdf}'.")

# Specify the directory path where your PDF files are located
directory_path = "pdf"

# Call the merge_pdfs function with the specified directory path
merge_pdfs(directory_path)

