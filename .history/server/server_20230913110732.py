import socket
import tkinter as tk

# Define the host and port on which the server will listen
HOST = '127.0.0.1'
PORT = 8080

# Create the main application window
root = tk.Tk()
root.title("Concussion C3 Server")
root.geometry("400x300")  # Adjust the window size as needed

# Create a dark-blue theme with light-blue font
custom_theme = {
    "background": "#000080",  # Dark-blue background color
    "foreground": "#00FFFF",  # Light-blue font color
}

# Apply custom theme to the entire GUI
for element, color in custom_theme.items():
    root.option_add("*.{element}".format(element=element), color)

# Create a label for the server status
status_label = tk.Label(root, text="Server Status: Not Running")
status_label.pack(pady=10)

# Create a button to start the server
def start_server():
    # Add server start logic here
    status_label.config(text="Server Status: Running")

start_button = tk.Button(root, text="Start Server", command=start_server)
start_button.pack()

# Create a button to stop the server
def stop_server():
    # Add server stop logic here
    status_label.config(text="Server Status: Not Running")

stop_button = tk.Button(root, text="Stop Server", command=stop_server)
stop_button.pack()

# Run the GUI application
root.mainloop()
