import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from reportlab.pdfgen.canvas import Canvas
from PIL import Image, ImageFont, ImageDraw, ImageTk, ImageFile
from resizePhoto import resizeImage


JPEGfilepath = "sample.jpeg"

title_font = ImageFont.truetype('Montserrat ExtraBold.ttf', 81)
title_font2 = ImageFont.truetype('arial.ttf', 200)
title_text = "YRYSKELDI"

my_image = Image.open(JPEGfilepath)
my_image = my_image.convert('RGB')
image_editable = ImageDraw.Draw(my_image)
w = image_editable.textlength(title_text, font=title_font)
w2 = image_editable.textlength("0001", font=title_font2)
W, H = my_image.size

image_editable.text(((W - w2) / 2, 300), "0001", font=title_font2, fill=(255,255,255,128))
image_editable.text(((W - w) / 2, 550), title_text, font=title_font,  fill=(255,255,255,128))
image_editable.line((200, 100, 300, 200), fill=(255,255,255,128), width=10)

my_image.save("demo.jpeg")
print("done")
