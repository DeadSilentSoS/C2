import socket

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'  # The server's IP address
SERVER_PORT = 8080       # The port on which the server is listening

def main():
    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    print(f"Connected to {SERVER_IP}:{SERVER_PORT}")
    
    # Send a command to the server (for testing purposes)
    command = "Hello, server!"
    client_socket.send(command.encode('utf-8'))
    
    # Receive and print the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")
    
    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    main()
