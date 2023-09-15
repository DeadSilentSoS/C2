import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create the main application window
root = customtkinter.CTk()
root.title("Concussion C2 Client")
root.geometry("400x300")
root.resizable(True, True)  # Allow window resizing

# Customize the theme
customtkinter.set_appearance_mode("Dark")  # Change appearance mode
customtkinter.set_default_color_theme("blue")  # Change color theme

# Create a label for the server connection status
status_label = customtkinter.CTkLabel(root, text="Server Status: Not Connected")
status_label.pack(pady=10)

# Create an entry field for user input
command_entry = customtkinter.CTkEntry(root, width=40, placeholder_text="CTkEntry")
command_entry.pack()

# Create a function to send the command to the server
def send_command():
    command = command_entry.get()
    if command:
        # Add code to send the command to the server
        # You can use the SERVER_IP and SERVER_PORT here
        status_label.config(text="Server Status: Command Sent")

send_button = customtkinter.CTkButton(root, text="Send Command", command=send_command)
send_button.pack()

# Load and display an icon
icon_image = Image.open("client_icon.png")
tk_icon_image = ImageTk.PhotoImage(icon_image)
icon_label = customtkinter.CTkLabel(root, image=tk_icon_image)
icon_label.pack()

# Run the GUI application
root.mainloop()

