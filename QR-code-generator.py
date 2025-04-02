import qrcode

print("Welcome! You can generate a QR code for any text oe URL")

data = input("Enter the text or URL you want to encode: ").strip()
if not data:
    print("No data provided. Exiting...")
    exit(1)

fileName = input("Enter the filename to save the QR code: ").strip()
if not fileName:
    print("No filename provided. Exiting...")
    exit(1)

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(fill_color="black", back_color="white")
image.save(fileName + ".png")
print(f"QR code saved as {fileName}.png")
