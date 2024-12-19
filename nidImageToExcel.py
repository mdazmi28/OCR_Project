from operator import index
import pandas as pd
from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r".\input_images\NID2.png"

output_path = r'.\output_texts\NID_INFO.xlsx'

if os.path.exists(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    print(lines)
    data = {
        "Name" : lines[4].split("Name:")[-1].strip(),
        "DOB" : lines[-2].split("Date of Birth:")[-1].strip(),
        "ID No." : lines[-1].split("ID NO:")[-1].strip()
    }

    df = pd.DataFrame([data])

    if os.path.exists(output_path):
        existing_file = pd.read_excel(output_path)
        combined_df = pd.concat([existing_file,df],ignore_index=True)
    else:
        combined_df = df

    os.makedirs("./output_texts", exist_ok=True)
    combined_df.to_excel(output_path,index=False)
else:
    print("No file found")