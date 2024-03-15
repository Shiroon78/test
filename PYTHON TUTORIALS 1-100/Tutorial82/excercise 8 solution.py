from PyPDF2 import PdfWriter
import os

files = [files for file in os.listdir() if file.endswith('.pdf')]

merger = PdfWriter()

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()