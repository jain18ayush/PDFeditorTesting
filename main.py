from tkinter import *
from tkinter import Text
import PyPDF2
from tkinter import Menu
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog as fd
from tokenize import String

from tkPDFViewer import tkPDFViewer as pdf


root = Tk()
root.title('pdf editor')
root.geometry("500x500")

var1 = pdf.ShowPdf()

left_text = Text(root, height=30, width=30)
left_text.pack(side=RIGHT)

var2=var1.pdf_view(root,pdf_location=f"Attestation-form-Minor-applicant5.pdf",bar=True,load="after",zoomDPI=72)
var2.pack()
root.mainloop()