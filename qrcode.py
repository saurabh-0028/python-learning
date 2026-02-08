!pip install qrcode
import qrcode

data = input("Enter text to convert into QR code: ")
qr = qrcode.make(data)

file_name = input("Enter file name (without extension): ")
qr.save(file_name + ".png")

print("QR Code saved as", file_name + ".png")