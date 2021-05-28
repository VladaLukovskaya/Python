import random

pixel_array = [[[random.randrange(1, 255, 1) for i in range(3)] for j in range(3)] for k in range(3)]


def image_filter(pixels, i, j):
    """Changing a pixel color to white or black"""
    r = pixels[i][j][0]
    g = pixels[i][j][1]
    b = pixels[i][j][2]
    s = r + g + b
    index = 10

    if s > (((255 + index) // 2) * 3):
        r, g, b = 255, 255, 255
    else:
        r, g, b = 0, 0, 0
    return r, g, b


image_filter(pixel_array, 0, 2)
