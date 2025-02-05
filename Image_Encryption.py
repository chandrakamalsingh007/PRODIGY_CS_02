from PIL import Image

def encrypt_image(image_path, key):
    # Open image from given image path
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Encrypt the image by applying a basic mathematical operation to each pixel and swapping
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    # Save the encrypted image
    encrypted_image_path = image_path.replace('.', '_encrypted.')
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}.")

def decrypt_image(encrypted_image_path, key):
    # Open image from the given encrypted image path
    img = Image.open(encrypted_image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Decrypt the image by applying a reverse mathematical operation to each pixel and swapping
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    # Save the decrypted image
    decrypted_image_path = encrypted_image_path.replace('_encrypted.', '_decrypted.')
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}.")

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            image_path = input("Enter the path of the image to encrypt: ")
            encryption_key = 77
            encrypt_image(image_path, encryption_key)

        elif choice == '2':
            encrypted_image_path = input("Enter the path of the image to decrypt: ")
            encryption_key = 77
            decrypt_image(encrypted_image_path, encryption_key)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
