# Generate
import pyqrcode

ssid = "Ye Olde Guest Access"
password = "ZuGaBe81RoSt"
security = "WPA"

qrcode = pyqrcode.create(b'WIFI:S:Ye Olde Guest Access;T:WPA;P:ZuGaBe81RoSt;;')
print(qrcode.png("images/qrcode.png", scale=6))

# Decode
from PIL import Image
from pyzbar.pyzbar import decode

data = decode(Image.open("images/test.png"))
data2= decode(Image.open("images/qrcode.png"))
print(data)
print(data2)

