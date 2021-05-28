from PIL import Image


def make_preview(size, n_colors):
    new_image = Image.open('an_image.jpg')
    new_image = new_image.resize(size)
    new_image = new_image.quantize(n_colors)
    # new_image.show()
    new_image.save('res.bmp')


make_preview((400, 200), 64)
