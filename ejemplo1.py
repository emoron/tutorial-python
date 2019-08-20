from PIL import Image
import os
import sys
folder = "Fotos\\"
size = (100,100)
for infile in sys.argv[1:]: #Lo que le paso en la linea de comandos (ejemplo: run arg1 arg2)
    output = os.path.splitext(infile)[0]+".jpg"
    try:
        im= Image.open(folder+infile)
#        im.thumbnail(size)
#        im.save(output, "JPEG")

        region = (100,100,300,300)
        corte = im.crop(region)
#        im2 = corte.transpose(Image.ROTATE_180)
        im2.save(output, "JPEG")
    except IOError:
        print('mal')
