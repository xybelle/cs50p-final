import os
import sys

from PIL import Image, ImageOps


valid_extensions = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]


def main():
    # Ensure user provide two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments\nUsage: python shirt.py input output")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments\nUsage: python shirt.py input output")

    temp_a = os.path.splitext(sys.argv[1])
    temp_b = os.path.splitext(sys.argv[2])
    if temp_a[1] != temp_b[1]:
        sys.exit("Input and output have different extensions")

    if temp_a[1] not in valid_extensions and temp_b[1] not in valid_extensions:
        sys.exit("Invalid input or output extension(s)")

    resize_image()


def resize_image():
    shirt = Image.open("shirt.png")
    size = shirt.size
    model = Image.open(sys.argv[1])
    try:
        new_image = ImageOps.fit(model, size=size)
        save_image(shirt, new_image)
    except FileNotFoundError:
        sys.exit(f"Cannot open {sys.argv[1]}")


def save_image(shirt, new_image):
    new_image.paste(shirt, shirt)
    new_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
