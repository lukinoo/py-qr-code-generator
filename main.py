import pyqrcode

# String which represents the QR code
s = input("Enter any word: ")

# Generate QR code
url = pyqrcode.create(s)

# creating and saving the svg file
url.svg("./assets/QR.svg", scale=7)