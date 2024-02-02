import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    checking_argv()
    # Open the image
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open Shirt
    shirtfile = Image.open("shirt.png")
    # Get the size of t he shirt
    size = shirtfile.size
    # Resize the muppet image to fit with the muppet image
    muppet = ImageOps.fit(imagefile, size)
    # Paste shirt in muppet
    muppet.paste(shirtfile, shirtfile)
    # Create output image
    muppet.save(sys.argv[2])
def checking_argv():
    # Check how many elements in the comman line
    if len(sys.argv) > 3:
        sys.exit(" Too many command-line argumeents")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    # Check if it is a image file
    if extension(file1[1]) == False:
        sys.exit("Invalid input")
    if extension(file2[1]) == False:
        sys.exit("Invalid output")
    # Check if extention of both files are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")
def extension(file):
    if file in [".jpg", "jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()

#This is the original file that is working!
