from PIL import Image
image = Image.open("xlsx/super_mario_grayscale.bmp")

def luminance_to_bw(luminance, threshold=128):
    if luminance < threshold:
        return 0
    else:
        return 1

w, h = image.size
bw_values = []
for y in range(h):
    for x in range(w):
        grayscale_value = image.getpixel((x, y))
        bw = luminance_to_bw(grayscale_value, 128)
        bw_values.append(bw)

print(f"Black and white bitmap with {len(bw_values)} pixel values: {bw_values}")

bw_image = Image.new("1", (w, h))
bw_image.putdata(bw_values)
bw_image.save("xlsx/super_mario_bw.bmp")