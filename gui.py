import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageFont, ImageDraw, ImageTk, ImageFile
import pandas as pd
import math
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger, PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas
from demo import runDemo
from resizePhoto import resizeImage
from PIL.ImageFilter import DETAIL

def openJPEG():
    global JPEGfilepath
    JPEGfilepath = filedialog.askopenfilename()

def openXLS():
    global XLSfilepath
    XLSfilepath = filedialog.askopenfilename()

def run():
    data = pd.read_excel(XLSfilepath)
    cols = data.columns
    numlist = list(int(x) for x in data[cols[0]] if math.isnan(x) == False)
    namelist = list(x for x in data[cols[4]])
    for x in range(10):
        print(x)
        my_image = Image.open(JPEGfilepath)
        my_image = my_image.convert('RGB')
        title_font = ImageFont.truetype('fonts/Montserrat ExtraBold.ttf', int(name_value.get()))
        title_font2 = ImageFont.truetype('fonts/Montserrat-Bold.ttf', int(id_value.get()))
        title_text = namelist[x]

        image_editable = ImageDraw.Draw(my_image)
        w = image_editable.textlength(title_text, font=title_font)
        w2 = image_editable.textlength(str(numlist[x]), font=title_font2)
        W, H = my_image.size

        COLORS = (255, 255, 255)

        image_editable.text(((W - w) / 2, int(height2.get())), title_text, fill=COLORS, font=title_font, dpi=(300, 300), quality=100)
        image_editable.text(((W - w2) / 2, int(height1.get())), str(numlist[x]), fill=COLORS, font=title_font2, dpi=(300, 300), quality=100)
        my_image.save("media/temp.jpeg", dpi=(300, 300), quality=100)
        resizeImage('media/temp.jpeg', 826, 583) #826, 583
        my_image = Image.open('media/resized.jpg')
        my_image = my_image.filter(DETAIL)
        my_image.save('media/test.pdf', "PDF", resolution=100.0, save_all=True, dpi=(300, 300), quality=100)
        merge_pdfs()
    infile = PdfReader('media/res.pdf', 'rb')
    output = PdfWriter()

    for i in range(1, len(infile.pages)):
        p = infile.pages[i]
        output.add_page(p)

    with open('media/res.pdf', 'wb') as f:
        output.write(f)

    reader = PdfReader('media/res.pdf')
    print(reader.pages[0].mediabox)
    print("done")

def merge_pdfs():
    merger = PdfFileMerger()

    merger.append(PdfFileReader("media/res.pdf"))
    merger.append(PdfFileReader("media/test.pdf"))

    merger.write("media/res.pdf")


def create_button_frame(container):
    frame = ttk.Frame(container, padding=10, relief="solid")

    frame.columnconfigure(0, weight=1)

    ttk.Label(frame, text='JPEG шаблон:').grid(column=0, row=0, sticky=tk.W)
    ttk.Button(frame, text='Открыть файл', command=openJPEG).grid(column=0, row=1)

    ttk.Label(frame, text='Excel:').grid(column=0, row=2, sticky=tk.W)
    ttk.Button(frame, text='Открыть файл', command=openXLS).grid(column=0, row=3)

    global height1 #307
    ttk.Label(frame, text='Высота текста (номер):').grid(column=0, row=4, sticky=tk.W)
    height1 = ttk.Entry(frame, width=15)
    height1.insert(0, 370)
    height1.grid(column=0, row=5)

    global id_value
    id_value = tk.StringVar(value=180)
    ttk.Label(frame, text='Размер текста:').grid(column=0, row=6, sticky=tk.W)
    s = ttk.Spinbox(frame, from_=1.0, to=400.0, width=15, textvariable=id_value).grid(column=0, row=7)

    global height2
    ttk.Label(frame, text='Высота текста (имя):').grid(column=0, row=8, sticky=tk.W)
    height2 = ttk.Entry(frame, width=15)
    height2.insert(0, 550)
    height2.grid(column=0, row=9)

    global name_value
    name_value = tk.StringVar(value=81)
    ttk.Label(frame, text='Размер текста:').grid(column=0, row=10, sticky=tk.W)
    s = ttk.Spinbox(frame, from_=1.0, to=400.0, width=15, textvariable=name_value).grid(column=0, row=11)

    ttk.Button(frame, text='Применить', command=lambda: runDemo(JPEGfilepath, id_value.get(),\
                                            name_value.get(), height1.get(), height2.get())).grid(column=0, row=12)
    ttk.Button(frame, text='Сохранить', command=run).grid(column=0, row=13)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame