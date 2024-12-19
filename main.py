from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Image file path
image1 = r".\input_images\img_1.jpg"


# Check if the file exists
if os.path.exists(image1):
    text1 = pytesseract.image_to_string(Image.open(image1))
    base_name = os.path.basename(image1)
    file_name = base_name.split(".")[0]+".txt"
    output_path = os.path.join(r".\output_texts", file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the extracted text to the text file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text1)
else:
    print(f"File not found: {image1}")