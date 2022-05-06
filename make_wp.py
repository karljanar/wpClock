import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


base_dir = os.path.dirname(__file__)
src_img_path = os.path.join(base_dir, "img/src.png")
out_img_path = os.path.join(base_dir, "img/out.png")


font = ImageFont.truetype("NotoSansDisplay-BoldItalic.ttf", 90)
time = datetime.now().strftime("%H:%M")

im = Image.open(src_img_path)
imgWidth, imgHeight = im.size
draw = ImageDraw.Draw(im)
textWidth, textHeight = draw.textsize(time, font=font)
draw.text(((imgWidth-textWidth)/2,(imgHeight-textHeight)/2), time, font=font, fill="#E8A746")


im.save(out_img_path, quality=95)
