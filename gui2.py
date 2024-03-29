import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

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
        if self.image_input and self.mode in ["1. MODULAR ARITHMETIC ENCRYPTION", "2. XOR ENCRYPTION"] and self.text_input:
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

        
        if self.mode == "1. MODULAR ARITHMETIC ENCRYPTION":
            images = ["input.png", "input.png", "input.png", "input.png", "input.png", "input.png", ]  # Placeholder image for demonstration
        elif self.mode == "2. XOR ENCRYPTION":
            images = ["input.png", "input.png", "input.png"]  # Placeholder image for demonstration
        else:
            messagebox.showerror("Error", "Invalid mode.")
            return

        for image_path in images:
            image = Image.open(image_path)
            width, height = image.size
            new_width = width // int(self.text_input)
            new_height = height // int(self.text_input)
            resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
            photo_image = ImageTk.PhotoImage(resized_image)
            image_label = tk.Label(self.container, image=photo_image)
            image_label.photo = photo_image  # Keep a reference to prevent garbage collection
            image_label.pack(side="left", padx=10, pady=10)

if __name__ == "__main__":
    app = ImageDropGUI()
    app.mainloop()
