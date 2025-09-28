from PIL import Image, ImageFont, ImageDraw

font = ImageFont.truetype("C:\\Users\\nimeseth\\Downloads\\Barriecito\\Barriecito-Regular.ttf", 64)
img = Image.new("L", (200, 200), 0)
draw = ImageDraw.Draw(img)
draw.text((10, 10), "A", fill=255, font=font)
img.show()