from PIL import Image
from datetime import datetime
from guNAH import *

iw,ih=900,900
m00=circular(iw,ih,0.1,0.075)

img=Image.frombytes('RGB',(iw,ih),m00)
img.show()
img.save('img/%s.jpg'%datetime.today().strftime('%Y-%m-%d_%H%M%S'),'JPEG')
