from PIL import Image, ImageDraw

img = Image.new('RGB', (400, 400), "grey")

draw = ImageDraw.Draw(img)
draw.polygon(((100, 100), (300, 50), (225, 25)), fill="green")
draw.polygon(((175, 100), (225, 50), (200, 25)),
             outline="yellow")

img.save('image.png', 'PNG')