from PIL import Image
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'imagen.png')

i = Image.open(filename)

i.show()
