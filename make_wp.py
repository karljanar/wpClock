import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import subprocess
from crontab import CronTab
from screeninfo import get_monitors


base_dir = os.path.dirname(__file__)
base_image_path = os.path.join(base_dir, "src.png")
result_image_path = os.path.join(base_dir, "out.png")
font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf", 200)
time = datetime.now().strftime("%H:%M")

im = Image.open(base_image_path)
draw = ImageDraw.Draw(im)
draw.text((2877, 2030), time, font=font, fill="#E8A746")




im.save(result_image_path, quality=95)

uri = "'file://%s'" % result_image_path
try:
    SCHEMA = "org.gnome.desktop.background"
    KEY = "picture-uri"
    gsettings = Gio.Settings.new(SCHEMA)
    gsettings.set_string(KEY, uri)
except:
    args = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", uri]
    subprocess.Popen(args)