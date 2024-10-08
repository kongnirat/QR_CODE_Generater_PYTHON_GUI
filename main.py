import qrcode

img = qrcode.make('Hello world')
img.save("some_file.png")