import qrcode


img = qrcode.make('eva')
type(img)  # qrcode.image.pil.PilImage
img.save("eva.png")


#for advanced qrcode 

qr = qrcode.QRCode(     #use the QRCode class
    version=1,      #controls the size of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white") #change the color of the qr code

