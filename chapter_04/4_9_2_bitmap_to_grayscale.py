from PIL import Image
image = Image.open("xlsx/super_mario_color.bmp")

def rgb_to_luminance(rgb_tuple):
    r = rgb_tuple[0]
    g = rgb_tuple[1]
    b = rgb_tuple[2]

    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    luminance = round(luminance)
    return luminance

w, h = image.size
grayscale_values = []
for y in range(h):
    for x in range(w):
        r, g, b = image.getpixel((x, y))
        luminance = rgb_to_luminance((r, g, b))
        grayscale_values.append(luminance)

print(f"Grayscale bitmap with {len(grayscale_values)} pixel values: {grayscale_values}")

grayscale_image = Image.new("L", (w, h))
grayscale_image.putdata(grayscale_values)
grayscale_image.save("xlsx/super_mario_grayscale.bmp")