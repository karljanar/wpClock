import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

imgWidth = 2160
imgHeight = 1440
base_dir = os.path.dirname(__file__)
src_img_path = os.path.join(base_dir, "img/src.png")
out_img_path = os.path.join(base_dir, "img/out.png")

font = ImageFont.truetype("NotoSansDisplay-BoldItalic.ttf", 90)
time = datetime.now().strftime("%H:%M")

im = Image.open(src_img_path)
draw = ImageDraw.Draw(im)
w, h = draw.textsize(time, font=font)
draw.text(((imgWidth-w)/2,(imgHeight-h)/2), time, font=font, fill="#E8A746")


im.save(out_img_path, quality=95)
