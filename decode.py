from pyzbar.pyzbar import decode
from PIL import Image
d=decode(Image.open("download.png"))
print(d[0].data.decode())
