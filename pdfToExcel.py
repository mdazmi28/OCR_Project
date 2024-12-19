import pandas as pd
import fitz  # PyMuPDF
import tabula
import os

# Define the input PDF file
pdf_file = r".\input_images\Bill.pdf"

# Read tables from the PDF
read_pdf = tabula.read_pdf(pdf_file, pages="all")

# Open the PDF file using PyMuPDF
doc = fitz.open(pdf_file)

# Variable to store normal text from the PDF
des = ""

# Function to extract tables from the PDF and save them as an Excel file
def excel():
    if os.path.exists(pdf_file):
        base_name = os.path.basename(pdf_file) 
        file_name = base_name.split(".")[0] + ".xlsx"
        output_path = os.path.join(r'.\output_texts', file_name)

        # Write the extracted tables to an Excel file
        with pd.ExcelWriter(output_path) as writer:
            for table in read_pdf:
                table_df = pd.DataFrame(table) 
                table_df.to_excel(writer, index=False)  

def normal_text():
    global des  
    if os.path.exists(pdf_file):  
        base_name = os.path.basename(pdf_file) 
        file_name = base_name.split(".")[0] + ".xlsx"  
        output_path = os.path.join(r'.\output_texts', file_name)  

        # Extract text from each page of the PDF
        for page in doc:
            des += page.get_text()  

        # Save the extracted text to an Excel file
        df = pd.DataFrame({'Text': [des]})  
        df.to_excel(output_path, index=False)
        # print(f"Text has been extracted and saved to {output_path}")

# Call the functions
# normal_text()
excel() 

