from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()

pdfEven = PdfFileReader(open('test2.pdf', 'rb'))
pdfOdd = PdfFileReader(open('test.pdf', 'rb'))

for i in range(pdfEven.getNumPages()):
    page = pdfEven.getPage(i)
    output.addPage(page)
    page = pdfOdd.getPage(pdfOdd.getNumPages() - 1 - i)
    output.addPage(page)

with open('newfile.pdf', 'wb') as f:
    output.write(f)