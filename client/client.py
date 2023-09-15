import tkinter as tk

# Define the server's IP address and port
HOST = '127.0.0.1'
PORT = 8080

# Create the main application window
root = tk.Tk()
root.title("Concussion C2 Client")
root.geometry("400x300")  # Adjust the window size as needed

# 1. Use a Consistent Color Scheme
primary_color = "#3498db"
secondary_color = "#2ecc71"
background_color = "#f2f2f2"
text_color = "#333333"

root.configure(bg=background_color)

# 2. Add Labels and Headings
main_heading = tk.Label(root, text="Concussion C2 Client", font=("Helvetica", 16, "bold"), bg=primary_color, fg=text_color)
main_heading.pack(pady=(20, 10))

# Placeholder for the send_command function
def send_command():
    command = command_var.get()  # Get the text from the entry
    if command and command != "Enter your command":  # Check if it's not empty or the default text
        # Add code to send the command to the server
        status_label.config(text="Server Status: Command Sent")

# Function to handle icon button event
def icon_button_event():
    # Add code to handle the icon button click event
    pass

# Create a label for the server connection status
status_label = tk.Label(root, text="Server Status: Not Connected", bg=background_color)
status_label.pack(pady=10)

# Create an entry field for user input
command_var = tk.StringVar()  # Create a StringVar to hold the entry text
command_var.set("Enter your command")  # Set the default text
command_entry = tk.Entry(root, width=40, font=("Helvetica", 12), bg="#ffffff", textvariable=command_var)
command_entry.pack()

# 3. Improve Button Styling
send_button = tk.Button(root, text="Send Command", bg=secondary_color, fg=text_color, command=send_command)
send_button.pack()

# 4. Incorporate Icons (Replace with your icon)
icon_image = tk.PhotoImage(file="C:/Users/noone/Desktop/Projects/C2/Misc/icon.png")
icon_button = tk.Button(root, image=icon_image, text="Icon Button", compound="left", bg=primary_color, fg=text_color, command=icon_button_event)
icon_button.image = icon_image  # Store a reference to the image
icon_button.pack(pady=20)

# Run the GUI application
root.mainloop()
