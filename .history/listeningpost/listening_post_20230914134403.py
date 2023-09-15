import tkinter as tk
import socket

# Define the IP address and port for the listening post
LISTENING_IP = '0.0.0.0'
LISTENING_PORT = 8081

# Create the main application window
root = tk.Tk()
root.title("Concussion Listening Post")
root.geometry("400x300")  # Adjust the window size as needed

# Create a dark-blue theme with light-blue font
custom_theme = {
    "background": "#000080",  # Dark-blue background color
    "foreground": "#00FFFF",  # Light-blue font color
}

# Apply custom theme to the entire GUI
for element, color in custom_theme.items():
    root.option_add("*.{element}".format(element=element), color)

# Create a label for the listening post status
status_label = tk.Label(root, text="Listening Post Status: Not Running")
status_label.pack(pady=10)

# Create a button to start the listening post
def start_listening_post():
    try:
        # Create a socket to listen for incoming connections
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((LISTENING_IP, LISTENING_PORT))
        server_socket.listen(1)  # Listen for a single connection

        # Accept a connection and print client information
        client_socket, client_address = server_socket.accept()
        status_label.config(text=f"Listening Post Status: Running\nClient Connected: {client_address}")

        # Add code to handle incoming commands from the client
        while True:
            command = client_socket.recv(1024).decode()
            if not command:
                break  # If the client closes the connection
            # Add your code to handle the command here
            
        # Close the client socket and the server socket
        client_socket.close()
        server_socket.close()

    except Exception as e:
        status_label.config(text=f"Listening Post Status: Error: {str(e)}")

start_button = tk.Button(root, text="Start Listening Post", command=start_listening_post)
start_button.pack()

# Create a button to stop the listening post
def stop_listening_post():
    # Add code to stop the listening post
    status_label.config(text="Listening Post Status: Not Running")

stop_button = tk.Button(root, text="Stop Listening Post", command=stop_listening_post)
stop_button.pack()

# Run the GUI application
root.mainloop()
