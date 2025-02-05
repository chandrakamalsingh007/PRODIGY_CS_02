# PRODIGY_CS_02
# Pixel manipulation for image encryption-Task-02

# Image Encryption and Decryption

This Python project provides a simple implementation of image encryption and decryption using the `PIL` (Python Imaging Library) module. The program allows you to encrypt and decrypt images by applying basic mathematical operations on pixel values.

## Features

- **Encrypt an image**: The program reads an image and applies a mathematical operation to the RGB values of each pixel, then swaps the color channels to encrypt the image.
- **Decrypt an image**: The program reverses the encryption process by applying the inverse operation and swapping the channels back to decrypt the image.
- **Simple key-based encryption**: The encryption key can be customized to generate different encrypted images.

## Limitations

- **Lost its pixel value while decrypting the encrypted image**: The program lost some of pixels value of r,g,b due to which a bit of distortion in image is present due to which exact image is not restored.

## Prerequisites

- Python 3.x
- `Pillow` (Python Imaging Library)

You can install the required dependencies by running:

```bash
pip install Pillow

### Steps
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/chandrakamalsingh007/PRODIGY_CS_02.git
2. Navigate to the project directory:
   
   cd PRODIGY_CS_02
3. Run the project:
   
   python3 ./Image_Encryption.py 
4. start as 
    Choose an option:
    1. Encrypt an image
    2. Decrypt an image
    3. Quit
    Enter choice (1/2/3):
   
Options
Encrypt an image:

Enter the path of the image file you want to encrypt.
The program will encrypt the image and save it with "_encrypted" appended to the original filename.
Decrypt an image:

Enter the path of the encrypted image.
The program will decrypt it and save it with "_decrypted" appended to the original filename.
Quit: Exit the program.

Example
Encrypting an image:

Choose an option:
1. Encrypt an image
2. Decrypt an image
3. Quit
Enter choice (1/2/3): 1
Enter the path of the image to encrypt: image.jpg
Image encrypted and saved as image_encrypted.jpg.

Decrypting an image:

Choose an option:
1. Encrypt an image
2. Decrypt an image
3. Quit
Enter choice (1/2/3): 2
Enter the path of the image to decrypt: image_encrypted.jpg
Image decrypted and saved as image_decrypted.jpg.

How It Works
Encryption:
Each pixel's RGB values are incremented by a constant key value and then wrapped around within the range of [0, 255] using modulo 256.
After this, the color channels are swapped (RGB -> BGR).
Decryption:
The reverse operation is applied by subtracting the key value and adjusting the color channels back (BGR -> RGB).



