import tkinter as tk
import socket

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
        try:
            # Create a socket to connect to the server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((SERVER_IP, SERVER_PORT))

            # Send the command to the server
            client_socket.send(command.encode())

            # Receive and display the server's response (modify as needed)
            response = client_socket.recv(1024).decode()
            status_label.config(text=f"Server Status: Response: {response}")

            # Close the socket
            client_socket.close()
        except Exception as e:
            status_label.config(text=f"Server Status: Error: {str(e)}")

send_button = tk.Button(root, text="Send Command", command=send_command)
send_button.pack()

# Run the GUI application
root.mainloop()
