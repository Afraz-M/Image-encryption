from modules.ModularArithmetic import *
from modules.XOR import *
import string
import random


def main():
    print("ENCRYPT YOUR IMAGE NOW!!!")
    while True:
        print("CHOOSE FROM ONE OF THE FOLLOWING METHODS TO ENCRYPT YOUR IMAGE")
        print("1. MODULAR ARITHMETIC BASED ENCRYPTION")
        print("2. XOR BASED ENCRYPTION")
        print("3. AES BASED ECNRYPTION")
        print("4. DONE")
        choice = input("CHOOSE ONE (1-4): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            print("UNTIL NEXT TIME.....")
            break
        else:
            print("OOPS SEEMS LIKE A WRONG NUMBER.. LET'S TRY AGAIN")


def option_1():
    print("YOU SELECTED MODULAR ARITHMETIC BASED ENCRYPTION")
    print("SELECT IMAGE TYPE")
    print("1. BINARY")
    print("2. GRAYSCALE")
    print("3. COLOUR")
    choice = input("CHOOSE ONE (1-3): ")

    if choice == "1":
        try:
            share_size = int(input("Input the number of shares images you want to create for encrypting (min is 2, max is 8) : "))
            if share_size < 2 or share_size > 8:
                raise ValueError
        except ValueError:
            print("Input is not a valid integer!")
            exit(0)

        try:
            image = input("Enter image path: ")
            input_image = Image.open(image).convert('1')
            print("After conversion", input_image)

        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

        print("Image uploaded successfully!")
        print("Input image size (in pixels) : ", input_image.size)   
        print("Number of shares image = ", share_size)

        shares, input_matrix = EncryptBinary_MA(input_image, share_size)
        for ind in range(share_size):
            image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
            name = "shares/Binary/MA/Share_" + str(ind+1) + ".png"
            image.save(name)

        output_image, output_matrix = DecryptBinary_MA(shares)
        output_image.save('Output/Binary/MA.png', mode = '1')
        print("Image is saved 'Output_Binary_MA.png' ...")

    elif choice == "2":
        try:
            share_size = int(input("Input the number of shares images you want to create for encrypting (min is 2, max is 8) : "))
            if share_size < 2 or share_size > 8:
                raise ValueError
        except ValueError:
            print("Input is not a valid integer!")
            exit(0)

        try:
            image = input("Enter image path: ")
            input_image = Image.open(image).convert('L')
            print("After conversion", input_image)

        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

        print("Image uploaded successfully!")
        print("Input image size (in pixels) : ", input_image.size)   
        print("Number of shares image = ", share_size)

        shares, input_matrix = EncryptGrayscale_MA(input_image, share_size)
        for ind in range(share_size):
            image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
            name = "shares/Grayscale/MA/Share_" + str(ind+1) + ".png"
            image.save(name)

        output_image, output_matrix = DecryptGrayscale_MA(shares)
        output_image.save('Output/Grayscale/MA.png', mode = '1')
        print("Image is saved 'Output_Grayscale_MA.png' ...")
        
    elif choice == "3":
        try:
            share_size = int(input("Input the number of shares images you want to create for encrypting (min is 2, max is 8) : "))
            if share_size < 2 or share_size > 8:
                raise ValueError
        except ValueError:
            print("Input is not a valid integer!")
            exit(0)

        try:
            image = input("Enter image path: ")
            input_image = Image.open(image)

        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

        print("Image uploaded successfully!")

        shares, input_matrix = EncryptColour_MA(input_image, share_size)
        for ind in range(share_size):
            image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
            name = "shares/Colour/MA/Share_" + str(ind+1) + ".png"
            image.save(name)

        output_image, output_matrix = DecryptColour_MA(shares)
        output_image.save('Output/Colour/MA.png', mode = '1')
        print("Image is saved 'Output_Colour_MA.png' ...")
        
    else:
        print("OOPS SEEMS LIKE A WRONG NUMBER.. LET'S TRY AGAIN")

def option_2():
    print("YOU SELECTED XOR BASED ENCRYPTION")
    print("SELECT IMAGE TYPE")
    print("1. BINARY")
    print("2. GRAYSCALE")
    print("3. COLOUR")
    choice = input("CHOOSE ONE (1-3): ")

    if choice == "1":
        try:
            share_size = int(input("Input the number of shares images you want to create for encrypting (min is 2, max is 8) : "))
            if share_size < 2 or share_size > 8:
                raise ValueError
        except ValueError:
            print("Input is not a valid integer!")
            exit(0)


        try:
            image = input("ENTER IMAGE PATH: ")
            input_image = Image.open(image).convert('1')

        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

        print("Image uploaded successfully!")
        print("Input image size (in pixels) : ", input_image.size)   
        print("Number of shares image = ", share_size)

        shares, input_matrix = EncryptBinary_XOR(input_image, share_size)

        for ind in range(share_size):
            image = Image.fromarray(shares[:,:,ind].astype(np.uint8))
            name = "shares/Binary/XOR/Share_" + str(ind+1) + ".png"
            image.save(name)

        output_image, output_matrix = DecryptBinary_XOR(shares)

        output_image.save('Output/Binary/XOR.png', mode= '1')
        print("Image is saved 'Output_Binary_XOR.png' ...")

    elif choice == "2":
        try:
            share_size = int(input("Input the number of shares images you want to create for encrypting (min is 2, max is 8) : "))
            if share_size < 2 or share_size > 8:
                raise ValueError
        except ValueError:
            print("Input is not a valid integer!")
            exit(0)

        try:
            image = input("ENTER IMAGE PATH: ")
            input_image = Image.open(image).convert('L')

        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

        print("Image uploaded successfully!")
        print("Input image size (in pixels) : ", input_image.size)   
        print("Number of shares image = ", share_size)

        shares, input_matrix = EncryptGrayscale_XOR(input_image, share_size)

        for ind in range(share_size):
            image = Image.fromarray(shares[:,:,ind].astype(np.uint8))
            name = "shares/Grayscale/XOR/Share_" + str(ind+1) + ".png"
            image.save(name)

        output_image, output_matrix = DecryptGrayscale_XOR(shares)

        output_image.save('Output/Grayscale/XOR.png')
        print("Image is saved 'Output_Grayscale_XOR.png' ...")

    elif choice == "3":
        try:
            share_size = int(input("Input the number of shares images you want to create for encrypting (min is 2, max is 8) : "))
            if share_size < 2 or share_size > 8:
                raise ValueError
        except ValueError:
            print("Input is not a valid integer!")
            exit(0)


        try:
            image = input("ENTER IMAGE PATH: ")
            input_image = Image.open(image)

        except FileNotFoundError:
            print("Input file not found!")
            exit(0)

        print("Image uploaded successfully!")
        print("Input image size (in pixels) : ", input_image.size)   
        print("Number of shares image = ", share_size)

        shares, input_matrix = EncryptColour_XOR(input_image, share_size)

        for ind in range(share_size):
            image = Image.fromarray(shares[:,:,:,ind].astype(np.uint8))
            name = "shares/Colour/XOR/Share_" + str(ind+1) + ".png"
            image.save(name)

        output_image, output_matrix = DecryptColour_XOR(shares)

        output_image.save('Output/Colour/XOR.png')
        print("Image is saved 'Output_Colour_XOR.png' ...")

    else:
        print("OOPS SEEMS LIKE A WRONG NUMBER.. LET'S TRY AGAIN")


def option_3():
    print("YOU SELECTED AES BASED ENCRYPTION")
    print("YOU SELECTED MODULAR ARITHMETIC BASED ENCRYPTION")
    image = input("ENTER IMAGE PATH: ")
    key = ''.join(random.choice(string.ascii_letters + string.digits +
                                           string.punctuation) for i in range(16))
    aes = AESImageEncryption()
    aes.encrypt(image, key)
    print("AES ENCRYPTION IS SUCCESFUL")
    aes.decrypt()
    print("AES DECRYPTION IS SUCCESSFUL")

if __name__ == "__main__":
    main()
