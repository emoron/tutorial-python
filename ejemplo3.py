from PIL import Image
import os
import sys

size = (100,100)

for infile in sys.argv[1:]:
    output = os.path.splitext(infile)[0]+"_miniatura.jpeg"
    print(os.path.splitext(infile))

    try:
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(output, "JPEG")

        region = (10,10,200,200)
        corte  = im.crop(region)
        im2 = corte.transpose(Image.ROTATE_180)
        output2 = os.path.splitext(output)[0]+'1.jpeg'
        im2.save(output2, 'JPEG')
    except IOError:
        print('Valio queso')
