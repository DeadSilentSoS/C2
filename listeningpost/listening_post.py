import socket

# Define the listening post's IP address and port
LISTENING_IP = '0.0.0.0'  # Listen on all available network interfaces
LISTENING_PORT = 8081     # Choose a port for the listening post

def main():
    # Create a socket and bind it to the specified address and port
    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_socket.bind((LISTENING_IP, LISTENING_PORT))
    
    # Listen for incoming connections
    listening_socket.listen(5)
    
    print(f"Listening Post is listening on {LISTENING_IP}:{LISTENING_PORT}")
    
    while True:
        # Accept incoming connections from clients
        client_socket, addr = listening_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        # Intercept and process traffic here (e.g., log data or redirect it)
        
        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    main()
