def toPNG(filename, remove=True):
    from PIL import Image

    avatar = Image.open(filename)
    avatar.save(filename + ".png",'png', optimize=True, quality=70)

    return filename + ".png"