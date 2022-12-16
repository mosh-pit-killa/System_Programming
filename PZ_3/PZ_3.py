from PIL import Image, ImageDraw

flag = Image.new('RGB', (300, 300), (255, 255, 255))

draw = ImageDraw.Draw(flag)

draw.rectangle((-1000, 100, 1000, 200), fill='blue', outline=(0, 0, 0))

draw.rectangle((-1000, 1000, 1000, 200), fill='red', outline=(0, 0, 0))

flag.save("flag.png", "PNG")

draw.text((10, 10), 'from Russia with <3', fill=('black'))

flag.save("text.png")