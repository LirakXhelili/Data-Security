from PIL import Image
import random

image_path = r'C:\Users\User\Desktop\Python\Picture1.png'
# Mapping of characters to colors
color_map = {
    "a": (255, 0, 0), # red
    "b": (0, 255, 0), # green
    "c": (0, 0, 255), # blue
    "d": (255, 255, 0), # yellow
    "e": (255, 0, 255), # magenta
    "f": (0, 255, 255), # cyan
    "g": (128, 0, 0), # maroon
    "h": (0, 128, 0), # dark green
    "i": (0, 0, 128), # navy
    "j": (128, 128, 0), # olive
    "k": (128, 0, 128), # purple
    "l": (0, 128, 128), # teal
    "m": (128, 0, 64), # crimson
    "n": (0, 128, 64), # forest green
    "o": (64, 0, 128), # indigo
    "p": (64, 128, 0), # olive green
    "q": (128, 64, 0), # brown
    "r": (128, 0, 1), # maroon
    "s": (0, 128, 128), # teal
    "t": (128, 128, 128), # gray
    "u": (255, 128, 0), # orange
    "v": (255, 0, 128), # pink
    "w": (0, 255, 128), # spring green
    "x": (128, 0, 255), # violet
    "y": (0, 255, 0), # lime green
    "z": (128, 128, 0) # olive
}


# Generate a random padding color
pad_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Encryption function
def encrypt_text(text):
    # Convert the text to lowercase and remove whitespace
    text = text.lower().replace(" ", "")

    # Determine the dimensions of the image
    width = len(text)
    height = width

    # Create a new image
    image = Image.new("RGB", (width, height), pad_color)

    # Map each character to a color and set the corresponding pixel
    for i, char in enumerate(text):
        color = color_map.get(char, pad_color)
        image.putpixel((i, i), color)

    return image
