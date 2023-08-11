import sys
from pdf2image import convert_from_path
a = sys.argv[1]
images = convert_from_path(a)

for i in range(len(images)):

    images[i].save(a[:-4] + ' page '+ str(i+1) +'.jpg', 'JPEG')

