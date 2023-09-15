import tkinter as tk
import socket
import threading

# Define the server's IP address and port
HOST = '127.0.0.1'
PORT = 8080

# Create the main application window
root = tk.Tk()
root.title("Concussion C3 Server")
root.geometry("400x300")  # Adjust the window size as needed

# 1. Use a Consistent Color Scheme
primary_color = "#3498db"
secondary_color = "#2ecc71"
background_color = "#000080"
text_color = "#333333"

root.configure(bg=background_color)

# 2. Add Labels and Headings
main_heading = tk.Label(root, text="Concussion C2 Server", font=("Helvetica", 16, "bold"), bg=primary_color, fg=text_color)
main_heading.pack(pady=(20, 10))

# Placeholder for the start_server function
def start_server():
    # Placeholder for server start logic
    status_label.config(text="Server Status: Running")

def icon_button_event():
    # Add code to handle the icon button click event
    pass

# Create a label for the server status
status_label = tk.Label(root, text="Server Status: Not Running", bg=background_color)
status_label.pack(pady=10)

# 3. Improve Button Styling
start_button = tk.Button(root, text="Start Server", bg=secondary_color, fg=text_color, command=start_server)
start_button.pack()

# 4. Enhance Entry Fields
command_entry = tk.Entry(root, width=40, font=("Helvetica", 12), bg="#ffffff")
command_entry.pack()

# 5. Incorporate Icons (Replace with your icon path)
icon_image = tk.PhotoImage(file="C:/Users/noone/Desktop/Projects/C2/Misc/icon.png")
icon_button = tk.Button(root, image=icon_image, text="Icon Button", compound="left", bg=primary_color, fg=text_color, command=icon_button_event)
icon_button.image = icon_image  # Store a reference to the image
icon_button.pack(pady=20)

# Run the GUI application
root.mainloop()
