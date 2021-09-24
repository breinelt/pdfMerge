from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog
import os


def get_all_unique_base_filenames(dir_path):
    files = os.listdir(dir_path)
    basenames = []
    for file in files:
        if "_Vorderseiten" in file:
            basename = file.split("_Vorderseiten")[0]
            basenames.append(basename)
    return sorted(set(basenames))


def get_all_documents(directory_path, output_directory):

    basenames = get_all_unique_base_filenames(directory_path)
    path_fronts = []
    path_backs = []
    path_output = []
    for basename in basenames:
        path_fronts.append(os.path.join(directory_path, ''.join([basename, "_Vorderseiten.pdf"])))
        path_backs.append(os.path.join(directory_path, ''.join([basename, "_Rückseiten.pdf"])))
        path_output.append(os.path.join(output_directory, ''.join([basename, ".pdf"])))

    return path_fronts, path_backs, path_output


def get_one_document():
    path_fronts = filedialog.askopenfilename(title='Fronts')
    path_backs = filedialog.askopenfilename(title='Backs')
    file_basename = os.path.split(path_fronts)[1].split("_Vorderseiten")[0]
    print(file_basename)
    path_output = filedialog.asksaveasfilename(title='Output', defaultextension='.pdf', filetypes=(("pdf", "*.pdf"),), initialfile=file_basename)

    return [path_fronts], [path_backs], [path_output]


def add_blank_pages_unless_even(even, odd):
    if even.getNumPages() < odd.getNumPages():
        even.insertBlankPage(width=578.16, height=824.4, index=0)
        add_blank_pages_unless_even(even, odd)
    elif even.getNumPages() > odd.getNumPages():
        odd.addBlankPage(width=578.16, height=824.4)
        add_blank_pages_unless_even(even, odd)


def main():
    root = tk.Tk()
    root.withdraw()

    directory_path = filedialog.askdirectory()
    output_directory = filedialog.askdirectory(title='Ausgabeverzeichnis', initialdir=directory_path, mustexist=True)
    path_fronts, path_backs, path_output = get_all_documents(directory_path, output_directory)

    for i, paths in enumerate(zip(path_fronts, path_backs, path_output)):
        fronts, backs, output_file = paths
        pdf_even = PdfFileReader(open(fronts, 'rb'))
        pdf_odd = PdfFileReader(open(backs, 'rb'))
        print("Start creating pdf: {}".format(output_file))

        # assert pdf_even.getNumPages() == pdf_odd.getNumPages()

        if not pdf_even.getNumPages() == pdf_odd.getNumPages():
            even = PdfFileWriter()
            even.cloneDocumentFromReader(pdf_even)
            odd = PdfFileWriter()
            odd.cloneDocumentFromReader(pdf_odd)
            add_blank_pages_unless_even(even, odd)

        output = PdfFileWriter()
        for i in range(pdf_even.getNumPages()):
            page = pdf_even.getPage(i)
            output.addPage(page)
            page = pdf_odd.getPage(pdf_odd.getNumPages() - 1 - i)
            output.addPage(page)

        with open(output_file, 'wb') as f:
            output.write(f)


if __name__ == "__main__":
    # execute only if run as a script
    main()
