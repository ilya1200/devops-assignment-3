from PIL import Image

img_name = "challenge.png"
mode = "RGB"
dim = (400, 500)
color = (255, 0, 0)

img = Image.new(mode, dim, color)
img.save(img_name)
