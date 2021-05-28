from PIL import Image, ImageDraw


def board(number, size):
    new_image = Image.new('RGB', (number * size, number * size), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    for i in range(number):
        for j in range(number):
            if i % 2 == 1 and j % 2 == 1 or i % 2 == 0 and j % 2 == 0:
                draw.rectangle([j * size, i * size, j * size + size - 1, i * size + size - 1], (0, 0, 0))
    # new_image.show()
    new_image.save('chess.png', 'PNG')


board(8, 50)
