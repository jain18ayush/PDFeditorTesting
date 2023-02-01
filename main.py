from tkinter import *
from tkinter import Text
import PyPDF2
from tkinter import Menu
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog
from tokenize import String

from tkPDFViewer import tkPDFViewer as pdf


root = Tk()
root.title('pdf editor')
root.geometry("500x500")

left_text = Text(root, height=30, width=30)
left_text.pack(side=RIGHT)

def open_pdf():
   file= filedialog.askopenfilename()
   if file:
     var1 = pdf.ShowPdf()
     var2=var1.pdf_view(root,pdf_location=f"Attestation-form-Minor-applicant5.pdf",bar=True,load="after",zoomDPI=72)
     var2.pack()

def clear_text():
   left_text.delete(1.0, END)

#Define function to Quit the window
def quit_app():
   root.destroy()

#Create a Menu
my_menu= Menu(root)
root.config(menu=my_menu)
#Add dropdown to the Menus
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text)
file_menu.add_command(label="Quit",command=quit_app)

root.mainloop()



