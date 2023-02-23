# File: traitement_image.py

from PIL import Image
import numpy as np
image = Image.open("image.jpg")

#rotate image
def rotate_image(image, angle):
    image = Image.open("image.jpg")
    image = image.rotate(angle)
    image.save("image_rotate.jpg")


#only red channel
def red_channel(image):
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = image.getpixel((i, j))
            image.putpixel((i, j), (r, 0, 0))
    red = image.save("image_red.jpg")
    return red

def main():
    rotated = rotate_image(image, 53)
    red_channel(rotated)

if __name__ == "__main__":
    main()
