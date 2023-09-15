import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

# Define the IP address and port for the listening post
LISTENING_IP = '0.0.0.0'
LISTENING_PORT = 8081

# Create the main application window
root = customtkinter.CTk()
root.title("Concussion Listening Post")
root.geometry("400x300")
root.resizable(True, True)  # Allow window resizing

# Customize the theme
customtkinter.set_appearance_mode("Dark")  # Change appearance mode
customtkinter.set_default_color_theme("blue")  # Change color theme

# Create a label for the listening post status
status_label = customtkinter.CTkLabel(root, text="Listening Post Status: Not Running")
status_label.pack(pady=10)

# Create a button to start the listening post
def start_listening_post():
    # Add code to start the listening post
    # You can use the LISTENING_IP and LISTENING_PORT here
    status_label.config(text="Listening Post Status: Running")

start_button = customtkinter.CTkButton(root, text="Start Listening Post", command=start_listening_post)
start_button.pack()

# Create a button to stop the listening post
def stop_listening_post():
    # Add code to stop the listening post
    status_label.config(text="Listening Post Status: Not Running")

stop_button = customtkinter.CTkButton(root, text="Stop Listening Post", command=stop_listening_post)
stop_button.pack()

# Load and display an icon
#icon_image = Image.open("listening_post_icon.png")
#tk_icon_image = ImageTk.PhotoImage(icon_image)
#icon_label = customtkinter.CTkLabel(root, image=tk_icon_image)
#icon_label.pack()

# Run the GUI application
root.mainloop()
