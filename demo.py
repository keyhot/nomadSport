import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from reportlab.pdfgen.canvas import Canvas
from PIL import Image, ImageFont, ImageDraw, ImageTk, ImageFile
from resizePhoto import resizeImage

def runDemo(JPEGfilepath, size2, size1, height1, height2):
    canvas = Canvas("media/res.pdf")
    canvas.drawString(72, 72, "i <3 NomadSport")
    canvas.save()

    title_font = ImageFont.truetype('fonts/Montserrat ExtraBold.ttf', int(size1))
    title_font2 = ImageFont.truetype('fonts/Montserrat-Bold.ttf', int(size2))
    title_text = "KUDAIBERGEN"

    my_image = Image.open(JPEGfilepath)
    my_image = my_image.convert('RGB')
    image_editable = ImageDraw.Draw(my_image)
    w = image_editable.textlength(title_text, font=title_font)
    w2 = image_editable.textlength("0123", font=title_font2)
    W, H = my_image.size

    COLORS = (255, 255, 255)

    image_editable.text(((W - w2) / 2, int(height1)), "0123", fill=COLORS, font=title_font2)
    image_editable.text(((W - w) / 2, int(height2)), title_text, fill=COLORS, font=title_font)

    my_image.save("media/demo.jpg")
    my_image.save("media/compare.jpg")
    resizeImage("media/demo.jpg")
    demoImage = Image.open("media/resized.jpg")

    canvas = tk.Canvas(width=900, height=620, bg='gray')
    canvas.grid(column=1, row=0, rowspan=15)

    img = ImageTk.PhotoImage(demoImage)
    canvas.create_image(
        0,
        0,
        image=img,
        anchor="nw"
    )
    canvas.image = img

