import customtkinter
from PIL import Image, ImageTk

# Load the icon image
icon_image = Image.open("server_icon.png")

# Convert the loaded image to a tkinter-compatible format
tk_icon_image = ImageTk.PhotoImage(icon_image)
# Create a label to display the icon
icon_label = customtkinter.CTkLabel(root, image=tk_icon_image)
icon_label.pack()
