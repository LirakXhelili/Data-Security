from PIL import Image
import random

image_path = r'C:\Users\Admin\Desktop\photo.jpg'
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

# Decryption function
def decrypt_text(image):
    # Determine the dimensions of the image
    width, height = image.size

    # Retrieve the color of each pixel along the diagonal
    colors = [image.getpixel((i, i)) for i in range(width)]

    # Map each color to a character and concatenate the results
    text = "".join([next((char for char, color in color_map.items() if color == c), "") for c in colors])

    return text

# Example usage
plaintext = "Pershendetje nga ne"
encrypted_image = encrypt_text(plaintext)
decrypted_text = decrypt_text(encrypted_image)

print("Plaintext: ", plaintext)
print("Encrypted image: ")
encrypted_image.show()
print("Decrypted text: ", decrypted_text)