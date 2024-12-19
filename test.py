# Python program for Business card Reader application  
# Import all necessary libraries  
import tkinter as tk  
from tkinter import filedialog  
from PIL import Image, ImageTk  
import pytesseract  

image_path = r".\input_images\NID2.png" 
def preprocess_image(image_path):  
    # For loading the image  
    image = Image.open(image_path)  
      
    # To convert the image to grayscale  
    gray_image = image.convert("L")  
    return gray_image  

# To perform OCR  
def perform_ocr(image):  
    # Perform OCR using Pytesseract  
    extracted_text = pytesseract.image_to_string(image, lang='eng')  
    return extracted_text  

def process_image():  
    # To open a file dialog and for selecting an image file  
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])  
    if file_path:  
        # For pre-processing the image  
        processed_image = preprocess_image(file_path)  
        # Performing OCR on the pre-processed image above  
        extracted_text = perform_ocr(processed_image)  
  
        # To display the extracted text in a new window  
        # Note: Required libraries like pytesseract need to be installed definitely  
        info_window = tk.Toplevel(root)  
        info_window.title("Extracted Contact Information")  
        text_widget = tk.Text(info_window)  
        text_widget.insert(tk.END, extracted_text)  
        text_widget.config(state=tk.DISABLED)  
        text_widget.pack()  

def open_image():  
    # Opens a file dialog and selects the image file  
    # file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])  
    file_path = r".\input_images\NID2.png" 
    if file_path:  
        # Displaying the selected image in the main window  
        image = Image.open(file_path)  
        image.thumbnail((400, 400))  # Resize the image to fit the window  
        img_label.image = ImageTk.PhotoImage(image)  
        img_label.config(image=img_label.image)  

# To create the main window and Title  
root = tk.Tk()  
root.title("Business Card Reader")  
  
# Creating buttons to open and process the selected image  
open_button = tk.Button(root, text="Open Image", command=open_image)  
process_button = tk.Button(root, text="Process Image", command=process_image)  

# Creating a label to display the image  
img_label = tk.Label(root)  
img_label.pack()  
open_button.pack()  
process_button.pack()  

root.mainloop()
