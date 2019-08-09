from PIL import Image, ImageEnhance

def main():
    
    filename = 'field.jpg'
    image = Image.open( filename )
    size = width, height = image.size
    
    if (image.mode == 'RGBA'):
        image.load()
        r, g, b, a = image.split( )
        image = Image.merge( 'RGB',( r, g, b))
        
    image.save( "mod_" + filename )
    del image

if ( __name__ == "__main__" ):
    main()
