import qrcode


img = qrcode.make(input("Add text or URL "))
type(img)  # qrcode.image.pil.PilImage
img.save(input("Add image file name ") + '.png')






