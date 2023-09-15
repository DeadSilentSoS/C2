import tkinter as tk
import socket
import threading

# Define the IP address and port for the listening post
LISTENING_IP = '0.0.0.0'
LISTENING_PORT = 8081

# Create the main application window
root = tk.Tk()
root.title("Concussion Listening Post")
root.geometry("400x300")  # Adjust the window size as needed

# 1. Use a Consistent Color Scheme
primary_color = "#3498db"
secondary_color = "#2ecc71"
background_color = "#f2f2f2"
text_color = "#333333"

root.configure(bg=background_color)

# 2. Add Labels and Headings
main_heading = tk.Label(root, text="Concussion Listening Post", font=("Helvetica", 16, "bold"), bg=primary_color, fg=text_color)
main_heading.pack(pady=(20, 10))

# Create a label for the listening post status
status_label = tk.Label(root, text="Listening Post Status: Not Running", bg=background_color)
status_label.pack(pady=10)

# Create a button to start the listening post
def start_listening_post():
    # Add code to start the listening post
    status_label.config(text="Listening Post Status: Running")

start_button = tk.Button(root, text="Start Listening Post", bg=secondary_color, fg=text_color, command=start_listening_post)
start_button.pack()

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
server_socket.bind((LISTENING_IP, LISTENING_PORT))
server_socket.listen()

print(f"Listening Post is listening on {LISTENING_IP}:{LISTENING_PORT}")

# Dictionary to store connected clients and their handlers
clients = {}

def start_listening_post():
    while True:
        # Accept incoming client connections
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client at {client_address}")

        # Add the client to the dictionary and start a handler thread
        clients[client_socket] = threading.Thread(target=handle_client, args=(client_socket,))
        clients[client_socket].start()

# ... (Rest of the GUI code)

# Run the GUI application
root.mainloop()
