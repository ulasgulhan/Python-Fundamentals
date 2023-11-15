from PIL import Image, ImageOps
import sys
import os


def argv_range(sys: int) -> bool:
    if len(sys) < 3:
        print('Too few command-line arguments')
        return False
    elif len(sys) > 3:
        print('Too many command-line arguments')
        return False
    else:
        return True



def edit_photo(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit('Input does not exist')


def main():
    length = argv_range(sys.argv)
    if length:
        format = ['.jpg', '.jpeg', '.png']
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit('Invalid output')
        elif inp[1].lower() != outp[1].lower():
            sys.exit('Input and output have different extensions')
        else:
            edit_photo(sys.argv[1], sys.argv[2])
    else:
        sys.exit()


main()