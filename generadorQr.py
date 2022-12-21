import qrcode
img = qrcode.make("Hola desde Recursos Python!")
f = open("output.png", "wb")
img.save(f)
f.close()