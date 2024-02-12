import os
import pandas as pd
from reportlab.pdfgen import canvas
from tkinter import filedialog

def detect_file_type(input_file):
    _, file_extension = os.path.splitext(input_file)
    file_extension = file_extension.lower()
    file_types = {
        '.txt': 'text',
        '.csv': 'csv',
        '.pdf': 'pdf'
    }
    return file_types.get(file_extension, "Le type de fichier d'entrée n'est pas pris en charge.")

def to_csv():
    input_file = filedialog.askopenfilename()
    if not input_file:
        return  
    output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
    if not output_file:
        return  
    file_type = detect_file_type(input_file)
    if file_type == 'text':
        text_to_csv(input_file, output_file)
    elif file_type == 'pdf':
        text_to_csv(input_file, output_file)

def to_pdf():
    input_file = filedialog.askopenfilename()
    if not input_file:
        return 
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Fichiers PDF", "*.pdf")])
    if not output_file:
        return 
    file_type = detect_file_type(input_file)
    if file_type == 'text':
        text_to_pdf(input_file, output_file)
    elif file_type == 'csv':
        csv_to_pdf(input_file, output_file)

def text_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()
    df = pd.DataFrame(data, columns=["Text"])
    df.to_csv(output_file, index=False)

def text_to_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.readlines()
    c = canvas.Canvas(output_file)
    y_coordinate = 800
    for line in data:
        c.drawString(15, y_coordinate, line.strip())
        y_coordinate -= 15  
    c.save()

def csv_to_pdf(input_file, output_file):
    df = pd.read_csv(input_file)
    c = canvas.Canvas(output_file)
    y_coordinate = 800
    for index, row in df.iterrows():
        c.drawString(15, y_coordinate, row[0])
        y_coordinate -= 15  
    c.save()