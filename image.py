from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("brad-pitt.jpg") as img:
        print(img.size)
        print(img.format)
        img = img.filter(ImageFilter.FIND_EDGES)
        img.save('brad-pitt-edges.jpg')


main()
