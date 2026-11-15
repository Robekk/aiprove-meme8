#!/usr/bin/env python3
"""Meme #10: 'A Floor, Not a Ceiling' — a robot standing on a floor
labelled '100' looking up a staircase labelled 107, 110, 120. PIL only."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H = 1200, 1200
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"
img = Image.new("RGB", (W, H), (14, 16, 32))
glow = Image.new("RGB", (W, H), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([560, 60, 1180, 500], fill=(40, 34, 14))
glow = glow.filter(ImageFilter.GaussianBlur(80))
img = ImageChops.add(img, glow)
d = ImageDraw.Draw(img, "RGBA")
GOLD = (222, 178, 74)
fT = ImageFont.truetype(FONT, 60)
fB = ImageFont.truetype(FONT, 44)
fS = ImageFont.truetype(FONT, 36)
fC = ImageFont.truetype(FONT, 42)

d.text((W // 2, 66), "A FLOOR, NOT A CEILING", font=fT, fill=(240, 205, 110), anchor="mm")

# staircase: three steps up to the right
d.polygon([(700, 1080), (1140, 1080), (1140, 900), (980, 900), (980, 720), (820, 720), (820, 540), (700, 540)], fill=(40, 38, 70), outline=GOLD, width=4)
d.text((1060, 1010), "120", font=fB, fill=(240, 205, 110), anchor="mm")
d.text((900, 830), "110", font=fB, fill=(240, 205, 110), anchor="mm")
d.text((760, 650), "107", font=fB, fill=(240, 150, 150), anchor="mm")
# step edge highlights
d.line([(700, 540), (820, 540)], fill=GOLD, width=6)
d.line([(980, 720), (820, 720)], fill=GOLD, width=6)
d.line([(1140, 900), (980, 900)], fill=GOLD, width=6)

# floor slab labelled 100
d.rounded_rectangle([60, 980, 760, 1100], radius=14, fill=(24, 20, 44), outline=GOLD, width=5)
d.text((410, 1040), "100", font=fB, fill=(240, 205, 110), anchor="mm")

# robot standing on the floor, looking up the stairs
rx, ry = 380, 820
d.rounded_rectangle([rx - 100, ry - 140, rx + 100, ry + 10], radius=30, fill=(196, 200, 210), outline=(70, 74, 88), width=5)
d.ellipse([rx - 60, ry - 96, rx - 18, ry - 54], fill=(30, 34, 48))
d.ellipse([rx + 18, ry - 96, rx + 60, ry - 54], fill=(30, 34, 48))
d.ellipse([rx - 48, ry - 84, rx - 30, ry - 66], fill=(120, 220, 255))
d.ellipse([rx + 30, ry - 84, rx + 48, ry - 66], fill=(120, 220, 255))
d.arc([rx - 32, ry - 48, rx + 32, ry + 2], start=15, end=165, fill=(30, 34, 48), width=6)
d.rectangle([rx - 12, ry - 186, rx + 12, ry - 140], fill=(120, 124, 140))
d.ellipse([rx - 22, ry - 212, rx + 22, ry - 172], fill=GOLD)
d.rounded_rectangle([rx - 74, ry + 10, rx + 74, ry + 130], radius=22, fill=(150, 156, 170), outline=(70, 74, 88), width=5)
d.rectangle([rx - 58, ry + 130, rx - 16, ry + 158], fill=(90, 94, 108))
d.rectangle([rx + 16, ry + 130, rx + 58, ry + 158], fill=(90, 94, 108))
# arm pointing up the stairs
d.line([(rx + 74, ry + 40), (rx + 210, ry - 60)], fill=(90, 94, 108), width=20)
d.ellipse([rx + 196, ry - 76, rx + 226, ry - 46], fill=(196, 200, 210), outline=(70, 74, 88), width=4)

d.text((W // 2, 1140), "the floor is built. now we climb.", font=fC, fill=(235, 235, 245), anchor="mm")
img.save("/home/hatch/workspace/aiprove/round8/meme10-floor-not-ceiling.png")
print("saved meme10")
