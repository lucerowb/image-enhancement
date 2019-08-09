from PIL import Image, ImageEnhance

def main():
    
    filename = 'field.jpg'
    image = Image.open( filename )
    size = width, height = image.size
    
    shrp =  ImageEnhance.Sharpness( image )

    image = shrp.enhance( 3.0 )

    cont = ImageEnhance.Contrast(image)


    img = cont.enhance(2.0)
    
    image.save( "mod1shrp_" + filename )
    img.save( "mod2con_" + filename)
    del image

if ( __name__ == "__main__" ):
    main()
