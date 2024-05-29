import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# from PIL import Image
import os
# function to convert images to PDF
def images_to_pdf(images, pdf_name):
    try:
        # create a new pdf file
        pdf = images.open(images[0])
        pdf.save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))
# function to select images
def select_images():
    images = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")), initialdir = "C:/")
    return images
# function to select pdf name and path
def select_pdf():
    pdf = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", initialdir = "C:/", filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    return pdf
# create GUI
root = tk.Tk()
root.title("Convert Images to PDF")
select_images_btn = tk.Button(root, text="Select Images", command=select_images)
select_pdf_btn = tk.Button(root, text="Select PDF", command=select_pdf)
convert_btn = tk.Button(root, text="Convert", command=lambda: images_to_pdf(select_images(), select_pdf()))
select_images_btn.pack()
select_pdf_btn.pack()
convert_btn.pack()
root.mainloop()


# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image

# # Function to convert images to PDF
# def images_to_pdf(images, pdf_name):
#     try:
#         # Open the first image and convert to RGB
#         image_list = []
#         for image in images:
#             img = Image.open(image)
#             if img.mode == 'RGBA':
#                 img = img.convert('RGB')
#             image_list.append(img)
        
#         if image_list:
#             # Save as PDF
#             image_list[0].save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=image_list[1:])
#             messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
#         else:
#             messagebox.showwarning("Warning", "No images to convert.")
#     except Exception as e:
#         messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))

# # Function to select images
# def select_images():
#     images = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")), initialdir="C:/")
#     return images

# # Function to select PDF name and path
# def select_pdf():
#     pdf = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", initialdir="C:/", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
#     return pdf

# # Create GUI
# root = tk.Tk()
# root.title("Convert Images to PDF")

# # Store selected images
# selected_images = []

# def select_images_handler():
#     global selected_images
#     selected_images = select_images()
#     if selected_images:
#         messagebox.showinfo("Selected Images", f"{len(selected_images)} images selected.")
#     else:
#         messagebox.showwarning("Warning", "No images selected.")

# def convert_handler():
#     if not selected_images:
#         messagebox.showwarning("Warning", "Please select images first.")
#         return
#     pdf_name = select_pdf()
#     if pdf_name:
#         images_to_pdf(selected_images, pdf_name)

# # Create buttons
# select_images_btn = tk.Button(root, text="Select Images", command=select_images_handler)
# convert_btn = tk.Button(root, text="Convert to PDF", command=convert_handler)

# # Layout buttons
# select_images_btn.pack(pady=10)
# convert_btn.pack(pady=10)

# root.mainloop()
