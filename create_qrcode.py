import create_qrcode

img = create_qrcode.make('this is another test')
type(img)
img.save('test.png')