from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()

# todo OpenFileDialog

pdfEven = PdfFileReader(open('test2.pdf', 'rb'))
pdfOdd = PdfFileReader(open('test.pdf', 'rb'))

# todo assert same number of pages

for i in range(pdfEven.getNumPages()):
    page = pdfEven.getPage(i)
    output.addPage(page)
    page = pdfOdd.getPage(pdfOdd.getNumPages() - 1 - i)
    output.addPage(page)

# todo SaveFileDialog

with open('newfile.pdf', 'wb') as f:
    output.write(f)