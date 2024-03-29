import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from modules.ModularArithmetic import *
from modules.XOR import *

class ImageDropGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Drop and Dropdown GUI")

        # Calculate the center of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 1000
        window_height = 700
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.container = tk.Frame(self)
        self.container.pack(expand=True, padx=20, pady=20)

        self.image_label = tk.Label(self.container, text="Drop image here", bg="lightgray")
        self.image_label.pack(pady=5)

        dropdown_frame = tk.Frame(self.container)
        dropdown_frame.pack(pady=5)

        self.dropdown_label = tk.Label(dropdown_frame, text="Encryption Mode:")
        self.dropdown_label.pack(side="left")

        self.dropdown_var = tk.StringVar(self)
        self.dropdown_var.set("Select Option")

        self.dropdown_menu = tk.OptionMenu(dropdown_frame, self.dropdown_var, "1. MODULAR ARITHMETIC ENCRYPTION", "2. XOR ENCRYPTION")
        self.dropdown_menu.pack(side="left", padx=5)

        dropdown_frame2 = tk.Frame(self.container)
        dropdown_frame2.pack(pady=5)

        self.dropdown_label2 = tk.Label(dropdown_frame2, text="Image Type:")
        self.dropdown_label2.pack(side="left")

        self.dropdown_var2 = tk.StringVar(self)
        self.dropdown_var2.set("Select Option")

        self.dropdown_menu2 = tk.OptionMenu(dropdown_frame2, self.dropdown_var2, "1. BINARY", "2. GRAYSCALE", "3. COLOUR")
        self.dropdown_menu2.pack(side="left", padx=5)

        text_entry_frame = tk.Frame(self.container)
        text_entry_frame.pack(pady=5)

        self.text_label = tk.Label(text_entry_frame, text="Enter Text:")
        self.text_label.pack(side="left")

        self.textbox = tk.Text(text_entry_frame, height=1, width=30)
        self.textbox.pack(side="left", padx=5)

        self.submit_button = tk.Button(self.container, text="START ENCRYPTION", command=self.submit_handler)
        self.submit_button.pack(pady=5)

        # Bind the drop_handler to the label
        self.image_label.bind("<Button-1>", self.drop_handler)

        # Initialize variables
        self.image_input = None
        self.mode = None

    def drop_handler(self, event):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.image_input = file_path
            self.update_image(file_path)

    def update_image(self, file_path):
        image = Image.open(file_path)
        width, height = image.size
        new_width = width // 3
        new_height = height // 3
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
        photo_image = ImageTk.PhotoImage(resized_image)

        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image

    def submit_handler(self):
        self.mode = self.dropdown_var.get()
        self.type = self.dropdown_var2.get()
        self.text_input = self.textbox.get("1.0", tk.END)
        if self.image_input and self.mode in ["1. MODULAR ARITHMETIC ENCRYPTION", "2. XOR ENCRYPTION"] and self.text_input and self.type in [ "1. BINARY", "2. GRAYSCALE", "3. COLOUR"]:
            print("Image Input:", self.image_input)
            print("Mode:", self.mode)
            self.display_images()
        else:
            messagebox.showerror("Error", "Please select an image and a mode.")

    def clear_previous_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def display_images(self):
        self.clear_previous_widgets(self.container)
        images = []
        if self.mode == "1. MODULAR ARITHMETIC ENCRYPTION":
            if self.type == "1. BINARY":
                try:
                    share_size = int(self.text_input)
                    if share_size < 2 or share_size > 8:
                        raise ValueError
                except ValueError:
                    print("Input is not a valid integer!")
                    exit(0)

                try:
                    image = self.image_input
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
                    images.append(name)
                    image.save(name)
                output_image, output_matrix = DecryptBinary_MA(shares)
                output_image.save('Output/Binary/MA.png', mode = '1')
                print("Image is saved 'Output/Binary/MA.png' ...")
            
            elif self.type == "2. GRAYSCALE":
                try:
                    share_size = int(self.text_input)
                    if share_size < 2 or share_size > 8:
                        raise ValueError
                except ValueError:
                    print("Input is not a valid integer!")
                    exit(0)

                try:
                    image = self.image_input
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
                    images.append(name)
                    image.save(name)

                output_image, output_matrix = DecryptGrayscale_MA(shares)
                output_image.save('Output/Grayscale/MA.png', mode = '1')
                print("Image is saved 'Output/Grayscale/MA.png' ...")                

            else:
                try:
                    share_size = int(self.text_input)
                    if share_size < 2 or share_size > 8:
                        raise ValueError
                except ValueError:
                    print("Input is not a valid integer!")
                    exit(0)

                try:
                    image = self.image_input
                    input_image = Image.open(image)

                except FileNotFoundError:
                    print("Input file not found!")
                    exit(0)

                print("Image uploaded successfully!")

                shares, input_matrix = EncryptColour_MA(input_image, share_size)
                for ind in range(share_size):
                    image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
                    name = "shares/Colour/MA/Share_" + str(ind+1) + ".png"
                    images.append(name)
                    image.save(name)

                output_image, output_matrix = DecryptColour_MA(shares)
                output_image.save('Output/Colour/MA.png', mode = '1')
                print("Image is saved 'Output/Colour/MA.png' ...")

        elif self.mode == "2. XOR ENCRYPTION":
            if self.type == "1. BINARY":
                try:
                    share_size = int(self.text_input)
                    if share_size < 2 or share_size > 8:
                        raise ValueError
                except ValueError:
                    print("Input is not a valid integer!")
                    exit(0)

                try:
                    image = self.image_input
                    input_image = Image.open(image).convert('1')
                    print("After conversion", input_image)

                except FileNotFoundError:
                    print("Input file not found!")
                    exit(0)

                print("Image uploaded successfully!")
                print("Input image size (in pixels) : ", input_image.size)   
                print("Number of shares image = ", share_size)

                shares, input_matrix = EncryptBinary_XOR(input_image, share_size)
                
                for ind in range(share_size):
                    image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
                    name = "shares/Binary/XOR/Share_" + str(ind+1) + ".png"
                    images.append(name)
                    image.save(name)
                output_image, output_matrix = DecryptBinary_XOR(shares)
                output_image.save('Output/Binary/XOR.png', mode = '1')
                print("Image is saved 'Output/Binary/XOR.png' ...")
            
            elif self.type == "2. GRAYSCALE":
                try:
                    share_size = int(self.text_input)
                    if share_size < 2 or share_size > 8:
                        raise ValueError
                except ValueError:
                    print("Input is not a valid integer!")
                    exit(0)

                try:
                    image = self.image_input
                    input_image = Image.open(image).convert('L')
                    print("After conversion", input_image)

                except FileNotFoundError:
                    print("Input file not found!")
                    exit(0)

                print("Image uploaded successfully!")
                print("Input image size (in pixels) : ", input_image.size)   
                print("Number of shares image = ", share_size)

                shares, input_matrix = EncryptGrayscale_XOR(input_image, share_size)
                for ind in range(share_size):
                    image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
                    name = "shares/Grayscale/XOR/Share_" + str(ind+1) + ".png"
                    images.append(name)
                    image.save(name)

                output_image, output_matrix = DecryptGrayscale_XOR(shares)
                output_image.save('Output/Grayscale/XOR.png', mode = '1')
                print("Image is saved 'Output/Grayscale/XOR.png' ...")                

            else:
                try:
                    share_size = int(self.text_input)
                    if share_size < 2 or share_size > 8:
                        raise ValueError
                except ValueError:
                    print("Input is not a valid integer!")
                    exit(0)

                try:
                    image = self.image_input
                    input_image = Image.open(image)

                except FileNotFoundError:
                    print("Input file not found!")
                    exit(0)

                print("Image uploaded successfully!")

                shares, input_matrix = EncryptColour_XOR(input_image, share_size)
                for ind in range(share_size):
                    image = Image.fromarray(shares[:,:,ind].astype(np.uint8) * 255)
                    name = "shares/Colour/XOR/Share_" + str(ind+1) + ".png"
                    images.append(name)
                    image.save(name)

                output_image, output_matrix = DecryptColour_XOR(shares)
                output_image.save('Output/Colour/XOR.png', mode = '1')
                print("Image is saved 'Output/Colour/XOR.png' ...")
        else:
            messagebox.showerror("Error", "Invalid mode.")
            return

        row_frame = None
        for idx, image_path in enumerate(images):
            if idx % 3 == 0:
                row_frame = tk.Frame(self.container)
                row_frame.pack(pady=5)

            image = Image.open(image_path)
            width, height = image.size
            new_width = width // 4
            new_height = height // 4
            resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
            photo_image = ImageTk.PhotoImage(resized_image)
            image_label = tk.Label(row_frame, image=photo_image)
            image_label.photo = photo_image
            image_label.pack(side="left", padx=10, pady=10)

        # Ensure the last row is properly packed
        if row_frame:
            row_frame.pack(fill="both", expand=True, pady=5)

if __name__ == "__main__":
    app = ImageDropGUI()
    app.mainloop()
