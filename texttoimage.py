from PIL import Image, ImageDraw, ImageFont
from iv import getSize
import numpy as np
import sys

# create new image
imgx = getSize()[0] # image width in pixels
imgy = getSize()[1] # image height in pixels
i = 1
phrases = ['ravioli ravioli',
            'pasta capiletti',
            'solid pasta food',
            'solidness solid dish']
for phrase in phrases:
    image = Image.new("RGB", (imgx, imgy),'white')
    font = ImageFont.truetype('comicsans.ttf',24) # load default bitmap font
    draw = ImageDraw.Draw(image)
    draw.text((10,imgy//3),phrase,font = font,fill='black')
    image.save("images/tmp/tmpt" + str(i) + ".png", "PNG")
    i += 1

list_im = ['images/tmp/tmpt1.png', 'images/tmp/tmpt2.png', 'images/tmp/tmpt3.png', 'images/tmp/tmpt4.png']
imgs = [Image.open(i) for i in list_im]
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

imgs_comb = np.vstack(np.asarray(i.resize(min_shape)) for i in imgs)
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('images/tmp/HStack.png')

list_im = ['images/tmp/VStack.jpg','images/tmp/HStack.png']
imgs = [Image.open(i) for i in list_im]
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

imgs_comb = np.hstack(np.asarray(i.resize(min_shape)) for i in imgs)
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save(sys.argv[1][:sys.argv[1].index('.')]+' IV.png')