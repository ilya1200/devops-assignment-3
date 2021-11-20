from PIL import Image, ImageColor

IMG_NAME = "chess_board.png"
MODE = "RGB"
SIZE = 8
COLOR_1 = "red"
COLOR_2 = "white"

DIM = (SIZE, SIZE)
img = Image.new(MODE, DIM)
pixels = img.load()

for i in range(SIZE):
    for j in range(SIZE):
        CELL_COLOR = COLOR_1 if (i + j) % 2 else COLOR_2
        pixels[i, j] = ImageColor.getcolor(CELL_COLOR, MODE)

img = img.resize((16 * SIZE, 16 * SIZE), Image.NEAREST)
img.save(IMG_NAME)
