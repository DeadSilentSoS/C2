import tkinter as tk
import socket
import threading

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

# Create the main application window
root = tk.Tk()
root.title("Concussion C2 Client")
root.geometry("400x300")  # Adjust the window size as needed

# 1. Use a Consistent Color Scheme
primary_color = "#000098"
secondary_color = "#2ecc71"
background_color = "#000080"
text_color = "#ffffff"

root.configure(bg=background_color)

# 2. Add Labels and Headings
main_heading = tk.Label(root, text="Concussion C2 Client", font=("Helvetica", 16, "bold"), bg=primary_color, fg=text_color)
main_heading.pack(pady=(20, 10))

# Create a label for the server connection status
status_label = tk.Label(root, text="Server Status: Not Connected", bg=background_color)
status_label.pack(pady=10)

# Create an entry field for user input
command_var = tk.StringVar()  # Create a StringVar to hold the entry text
command_var.set("Enter your command")  # Set the default text
command_entry = tk.Entry(root, width=40, font=("Helvetica", 12), bg="#ffffff", textvariable=command_var)
command_entry.pack()

# Placeholder for the send_command function
def send_command():
    command = command_var.get()  # Get the text from the entry
    if command and command != "Enter your command":  # Check if it's not empty or the default text
        # Add code to send the command to the server
        status_label.config(text="Server Status: Command Sent")

# 3. Improve Button Styling
send_button = tk.Button(root, text="Send Command", bg=secondary_color, fg=text_color, command=send_command)
send_button.pack()

# Function to handle individual client connections
def handle_client(client_socket):
    while True:
        # Receive a command from the client
        command = client_socket.recv(1024).decode('utf-8')

        if not command:
            break

        # Process the received command (e.g., execute it)
        # Add your command processing logic here

        # Send the response back to the client
        response = "Response to the command"
        client_socket.send(response.encode('utf-8'))

    # Remove the client from the dictionary when disconnected
    del clients[client_socket]
    client_socket.close()

# Create a socket and start listening for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()

print(f"C2 Server is listening on {SERVER_IP}:{SERVER_PORT}")

# Dictionary to store connected clients and their handlers
clients = {}

def start_server():
    while True:
        # Accept incoming client connections
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client at {client_address}")

        # Add the client to the dictionary and start a handler thread
        clients[client_socket] = threading.Thread(target=handle_client, args=(client_socket,))
        clients[client_socket].start()

# Run the GUI application
root.mainloop()
