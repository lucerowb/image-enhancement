import cv2
import numpy as np
from PIL import Image, ImageOps



filename = 'field.jpg'
image = Image.open( filename )
size = width, height = image.size

if ( image.mode == 'RGBA'):
    image.load()
    r, g, b, a = image.split( )
    image = Image.merge('RGB',(r, g, b))

image = ImageOps.autocontrast( image )
#a = np.asarray(vari)


#im = Image.fromarray(vari)
image.save('vari_' + filename)

