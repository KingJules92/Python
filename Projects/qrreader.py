'''
This small Project can be used to generate and decode qrcodes.
'''
# Generate
import pyqrcode

qrcode = pyqrcode.create('Hello World!')
print(qrcode.png("images\qrcode.png", scale=6))

# Decode
from PIL import Image
from pyzbar.pyzbar import decode

data2= decode(Image.open("images\qrcode.png"))

print(data2)
