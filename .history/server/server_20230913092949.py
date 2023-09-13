import socket

# Define the host and port on which the server will listen
HOST = '127.0.0.1'  # Listen on the loopback address
PORT = 8080         # Use port 8080 for communication

def main():
    # Create a socket and bind it to the specified address and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen(5)
    
    print(f"Listening on {HOST}:{PORT}")
    
    while True:
        # Accept incoming connections
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        # Handle communication with the client here
        
        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    main()
