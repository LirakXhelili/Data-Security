import cv2
import numpy as np
import string

# example usage
image_path = r'C:\Users\User\Desktop\Python\photo.jpg'
secret_message = 'This'
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-={}|[]\\:\";\',./<>?'


def encrypt_image(img_path, message, key, pad_color=(0, 0, 0)):
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    
    # create a mapping dictionary with color values based on the key
    mapping = {}
    for i, char in enumerate(key):
        b, g, r = np.random.randint(0, 256, 3)
        while (b, g, r) in mapping.values():
            b, g, r = np.random.randint(0, 256, 3)
        mapping[char] = (b, g, r)

    # convert message to binary string
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # pad message with specified color if needed
    pad_length = (h * w * 3) - len(binary_message)
    if pad_length < 0:
        raise ValueError("Message too long for image.")
    binary_message += ''.join(format(pad_color[i], '08b') for i in range(3)) * pad_length

    # modify the image with the mapping colors based on the binary message
    k = 0
    for i in range(h):
        for j in range(w):
            for c in range(3):
                if k < len(binary_message):
                    if binary_message[k] == '1':
                        img[i, j, c] = mapping[key[c]][c]
                    else:
                        img[i, j, c] = pad_color[c]
                    k += 1

    # save the modified image
    cv2.imwrite('encrypted_image.png', img)
    print('Message encrypted')

def decrypt(image_path, key):
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    message = ""
    mapping = dict(zip(key, string.ascii_lowercase))
    reverse_mapping = dict(zip(string.ascii_lowercase, key))
    for i in range(height):
        for j in range(width):
            color = tuple(img[i, j])
            if color in mapping:
                message += mapping[color]
            else:
                message += " "  # Default character
    return message

encrypt_image(image_path, secret_message, key)

encrypted_image_path = 'encrypted_image.png'
encrypted_message = decrypt(encrypted_image_path, key)
print('Decrypted message:', encrypted_message)
