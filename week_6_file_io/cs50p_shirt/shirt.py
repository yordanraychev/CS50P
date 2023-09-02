import sys, os
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    sys.exit("too many commnad-line arguments")
elif len(sys.argv) < 3:
    sys.exit("too few commnad-line arguments")
elif len(sys.argv) == 3:
    extentions = [".jpg", ".jpeg", ".png"]
    extention1 = os.path.splitext(sys.argv[1])
    extention2 = os.path.splitext(sys.argv[2])
    if extention1[1] == extention2[1] and extention1[1] in extentions:
        try:
            user_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File doesn't exist")
        shirt = Image.open("shirt.png")
        size = shirt.size
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])
    elif extention1[1] != extention2[1]:
        sys.exit("input and output have different extensions")
    else:
        sys.exit("wrong extention")
