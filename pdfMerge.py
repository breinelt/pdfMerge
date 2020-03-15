from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

output = PdfFileWriter()

# todo OpenFileDialog
path_fronts = filedialog.askopenfilename(title='Fronts')
path_backs = filedialog.askopenfilename(title= 'Backs')
path_output = filedialog.asksaveasfilename(title= 'Output', defaultextension='.pdf')

pdfEven = PdfFileReader(open(path_fronts, 'rb'))
pdfOdd = PdfFileReader(open(path_backs, 'rb'))

# todo assert same number of pages

for i in range(pdfEven.getNumPages()):
    page = pdfEven.getPage(i)
    output.addPage(page)
    page = pdfOdd.getPage(pdfOdd.getNumPages() - 1 - i)
    output.addPage(page)

# todo SaveFileDialog

with open(path_output, 'wb') as f:
    output.write(f)