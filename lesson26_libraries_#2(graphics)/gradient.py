from PIL.ImageDraw import Image, Draw

size_x = 512
size_y = 200

new_color = (0, 0, 0)
new_image = Image.new('RGB', (size_x, size_y), new_color)
draw = Draw(new_image)
for i in range(256):
    draw_line = draw.line((i*2, 0, i*2, 200), fill=(i, 0, 0), width=2)

# new_image.show()
new_image.save('image.png', 'PNG')
