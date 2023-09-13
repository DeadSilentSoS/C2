import tkinter as tk
import sockets

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create the main application window
root = tk.Tk()
root.title("Concussion C2 Client")
root.geometry("400x300")  # Adjust the window size as needed

# Create a dark-blue theme with light-blue font
custom_theme = {
    "background": "#000080",  # Dark-blue background color
    "foreground": "#00FFFF",  # Light-blue font color
}

# Apply custom theme to the entire GUI
for element, color in custom_theme.items():
    root.option_add("*.{element}".format(element=element), color)

# Create a label for the server connection status
status_label = tk.Label(root, text="Server Status: Not Connected")
status_label.pack(pady=10)

# Create an entry field for user input
command_entry = tk.Entry(root, width=40)
command_entry.pack()

# Create a function to send the command to the server
def send_command():
    command = command_entry.get()
    if command:
        # Add code to send the command to the server
        # You can use the SERVER_IP and SERVER_PORT here
        status_label.config(text="Server Status: Command Sent")

send_button = tk.Button(root, text="Send Command", command=send_command)
send_button.pack()

# Run the GUI application
root.mainloop()
