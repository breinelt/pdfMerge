from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

output = PdfFileWriter()

# todo OpenFileDialog
path_fronts = filedialog.askopenfilename(title='Fronts')
path_backs = filedialog.askopenfilename(title='Backs')

pdfFronts = PdfFileReader(open(path_fronts, 'rb'))
pdfBacks = PdfFileReader(open(path_backs, 'rb'))

# todo assert same number of pages
assert (pdfFronts.getNumPages() == pdfBacks.getNumPages()), 'Both documents have to have the same number of pages'

path_output = filedialog.asksaveasfilename(title='Output', filetypes=[('PDF files', '.pdf')], defaultextension='.pdf')


for i in range(pdfFronts.getNumPages()):
    page = pdfFronts.getPage(i)
    output.addPage(page)
    page = pdfBacks.getPage(pdfBacks.getNumPages() - 1 - i)
    output.addPage(page)

with open(path_output, 'wb') as f:
    output.write(f)