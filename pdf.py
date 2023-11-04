import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pyttsx3

def open_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        read_pdf_content(file_path)

def read_pdf_content(file_path):
    pdf = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf) 

    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    pdf.close()

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("PDF to Audio")

open_button = tk.Button(root, text="Open PDF", command=open_pdf_file)
open_button.pack(pady=20)

root.mainloop()
