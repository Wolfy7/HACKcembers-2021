from PIL import Image, ImageChops

size = 890, 500

rudolf = Image.open("#02/rudolf.png").convert("1", dither=Image.NONE)
klaus = Image.open("#02/klaus.png")

result = ImageChops.logical_xor(rudolf, klaus)

result.show()
