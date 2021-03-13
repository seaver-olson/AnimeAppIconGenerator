from os import replace, rename, remove
from PIL import Image, ImageDraw, ImageFilter

def create(folder):
    path = './icons/' + folder + '/'
    icon = path + 'icon.png'
    image = path + 'image.png'
    im1 = Image.open(icon)
    size = im1.size 
    im2 = Image.open(image)
    im2.convert('RGBA')
    if im2.size != size:
        im2 = im2.resize(size)
        remove(image)
        im2.save(image)
    alpha_composite = Image.alpha_composite(im1, im2)
    alpha_composite.save(path + 'final.png', 'png', quality=80)

