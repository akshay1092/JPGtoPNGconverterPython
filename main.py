from PIL import Image, ImageFilter
import sys
import os

if len(sys.argv) < 3 :
    print("invalid input")
    exit()

if not os.path.exists(sys.argv[1]):
    print(f" {sys.argv[1]} folder not exists!!!")
    exit()

if not os.path.exists(sys.argv[2]):
    os.mkdir(sys.argv[2])
    print(f"output folder {sys.argv[2]} created")

for filename in os.listdir(sys.argv[1]):
    img = Image.open(f"{sys.argv[1]}\{filename}")
    only_name =os.path.splitext(filename)[0]
    img.save(f"{sys.argv[2]}\{only_name}.png",'png')
