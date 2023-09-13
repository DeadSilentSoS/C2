# Payload Generator

# Template for the payload
payload_template = """
import socket

# Server IP and Port (customize these)
SERVER_IP = "{server_ip}"
SERVER_PORT = {server_port}

# Create a socket connection to the server
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        while True:
            command = input("Enter command: ")
            client_socket.send(command.encode())
            response = client_socket.recv(1024)
            print("Server response:", response.decode())
except Exception as e:
    print("Error:", str(e))
"""

# Function to generate a payload
def generate_payload(server_ip, server_port):
    return payload_template.format(server_ip=server_ip, server_port=server_port)

# Example usage
if __name__ == "__main__":
    server_ip = input("Enter server IP: ")
    server_port = int(input("Enter server port: "))
    
    payload = generate_payload(server_ip, server_port)
    with open("payload.py", "w") as file:
        file.write(payload)
    
    print("Payload generated as 'payload.py'")
