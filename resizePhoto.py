from PIL import Image
import PIL
def resizeImage(filepath, x = 0, y = 0):
    if x == 0 or y == 0:
        im = Image.open('demo.jpg')
        resized_im = im.resize((round(im.size[0]*0.68), round(im.size[1]*0.68)), resample=PIL.Image.Resampling.LANCZOS)
    else:
        im = Image.open(filepath)
        resized_im = im.resize((x ,y))
    resized_im.save('resized.jpg', dpi=(300, 300), quality=100)