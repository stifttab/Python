import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    if len(sys.argv) > 3:
        sys.exit(" Too many command-line argumeents")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if not extension(sys.argv[1]):
        sys.exit("Invalid input")
    if not extension(sys.argv[2]):
        sys.exit("Invalid output")

    image1 = splitext(sys.argv[1])
    image2 = splitext(sys.argv[2])

    if image1[1].lower() != image2[1].lower():
        sys.exit("Input and output have different extensions")

    try:
        main_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtfile = Image.open("shirt.png")

    size = shirtfile.size

    output_image = ImageOps.fit(main_image, size)

    output_image.paste(shirtfile, shirtfile)

    output_image.save(sys.argv[2])

def extension(filename):
    valid_extension = (".jpg", "jpeg", ".png")
    return splitext(filename)[1].lower() in valid_extension

if __name__ == "__main__":
    main()

#This is the code that i submitted to cs50!