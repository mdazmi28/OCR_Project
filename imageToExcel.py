import pandas as pd
from PIL import Image
import pytesseract
import os

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image file path
image_path = r".\input_images\img_2.jpg"

# Output Excel file path
output_path = r'.\output_texts\Contact_Info.xlsx'

# Check if image exists
if os.path.exists(image_path):
    # Extract text from the image
    extracted_text = pytesseract.image_to_string(Image.open(image_path))
    print(extracted_text)

    # Clean and filter the text: remove empty and extra lines
    lines = [line.strip() for line in extracted_text.split("\n") if line.strip()]
    
    # Parse the structured data
    data = {
        "Name": lines[0],
        "Designation": lines[1],
        "Department": lines[2],
        "Cell": lines[3].split("Cell")[-1].strip(),
        "Email": lines[4],
        "Company Name": lines[5],
        "Company Phone": lines[-3],
        "Company Email": lines[-2],
        "Website": lines[-1],
    }

    # Create a DataFrame with a single row
    df = pd.DataFrame([data])

    # Save to Excel
    os.makedirs("./output_texts", exist_ok=True)
    df.to_excel(output_path,index=False)

    print(f"Data saved to {output_path}")
else:
    print(f"File not found: {image_path}")