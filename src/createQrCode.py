from PIL import Image,ImageDraw,ImageFont
import qrcode

def createQrCode(data,location):
  qr_file = "qrCode.png"
  
  img = qrcode.make(data)
  img.save(f"{location}/{qr_file}")

  return qr_file