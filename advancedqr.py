import qrcode

#for advanced qrcode 

qr = qrcode.QRCode(     #use the QRCode class
    version=1,      #controls the size of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(input("Add text or URL "))
qr.make(fit=True)

img = qr.make_image(fill_color="#ff33cc", back_color="#29a329") #change the color of the qr code
img.save(input("Add image file name ") + '.png')
