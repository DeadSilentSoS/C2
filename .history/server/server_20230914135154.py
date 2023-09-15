import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

# Define the host and port on which the server will listen
HOST = '127.0.0.1'
PORT = 8080

# Create the main application window
root = customtkinter.CTk()
root.title("Concussion C3 Server")
root.geometry("400x300")
root.resizable(True, True)  # Allow window resizing

# Customize the theme
customtkinter.set_appearance_mode("Dark")  # Change appearance mode
customtkinter.set_default_color_theme("blue")  # Change color theme

# Create a label for the server status
status_label = customtkinter.CTkLabel(root, text="Server Status: Not Running")
status_label.pack(pady=10)

# Create a button to start the server
def start_server():
    # Add server start logic here
    status_label.config(text="Server Status: Running")

start_button = customtkinter.CTkButton(root, text="Start Server", command=start_server)
start_button.pack()

# Create a button to stop the server
def stop_server():
    # Add server stop logic here
    status_label.config(text="Server Status: Not Running")

stop_button = customtkinter.CTkButton(root, text="Stop Server", command=stop_server)
stop_button.pack()

# Load and display an icon
icon_image = Image.open("server_icon.png")
tk_icon_image = ImageTk.PhotoImage(icon_image)
icon_label = customtkinter.CTkLabel(root, image=tk_icon_image)
icon_label.pack()

# Run the GUI application
root.mainloop()
