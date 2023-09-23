import png
import pyqrcode
from pyqrcode import QRCode

link="https://youtu.be/qiQR5rTSshw"
test=pyqrcode.create(link)
test.png('network.png',scale=6)
