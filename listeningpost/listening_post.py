import tkinter as tk

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
    # Add code to start the listening post
    # You can use the LISTENING_IP and LISTENING_PORT here
    status_label.config(text="Listening Post Status: Running")

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

