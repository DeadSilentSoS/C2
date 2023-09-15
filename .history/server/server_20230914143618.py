import tkinter as tk
from PIL import Image, ImageTk

# Define the server's IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8080

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

# Create a label for the server connection status
status_label = tk.Label(root, text="Server Status: Not Connected", bg=background_color)
status_label.pack(pady=10)

# 3. Improve Button Styling
send_button = tk.Button(root, text="Send Command", bg=secondary_color, fg=text_color, command=send_command)
send_button.pack()

# 4. Enhance Entry Fields
command_entry = tk.Entry(root, width=40, font=("Helvetica", 12), bg="#ffffff", placeholder_text="Enter your command")
command_entry.pack()

# 5. Incorporate Icons
#icon_image = Image.open("icon.png")  # Replace with the path to your icon image
#icon_image = icon_image.resize((32, 32))  # Resize the icon as needed
#icon = ImageTk.PhotoImage(icon_image)

#icon_button = tk.Button(root, image=icon, text="Icon Button", compound="left", bg=primary_color, fg=text_color, command=icon_button_event)
#icon_button.image = icon  # Store a reference to the image
#icon_button.pack(pady=20)

# Rest of your code...

def send_command():
    command = command_entry.get()
    if command:
        # Add code to send the command to the server
        status_label.config(text="Server Status: Command Sent")

def icon_button_event():
    # Add code to handle the icon button click event
    pass

# Run the GUI application
root.mainloop()
