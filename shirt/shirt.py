import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    input_file, output_file = sys.argv[1], sys.argv[2]

    if not extension(input_file) or not extension(output_file):
        sys.exit("Input and output have different extensions")

    # Check how many elements in the comman line
    if len(sys.argv) > 3:
        sys.exit(" Too many command-line argumeents")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    image1 = splitext(input_file)
    image2 = splitext(output_file)

    # Open the image
    try:
        main_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open Shirt
    shirtfile = Image.open("shirt.png")
    # Get the size of t he shirt
    size = shirtfile.size
    # Resize the muppet image to fit with the muppet image
    output_image = ImageOps.fit(main_image, size)    
    # Paste shirt in muppet
    output_image.paste(shirtfile, shirtfile)
    # Create output image
    output_image.save(output_file)

def extension(filename):
    valid_extension = (".jpg", "jpeg", ".png")
    return splitext(filename)[1].lower() in valid_extension

if __name__ == "__main__":
    main()

