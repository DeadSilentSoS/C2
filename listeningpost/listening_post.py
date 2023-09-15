import tkinter as tk

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

# Function to start the listening post
def start_listening_post():
    # Add code to start the listening post
    # You can use the LISTENING_IP and LISTENING_PORT here
    status_label.config(text="Listening Post Status: Running")

# Function to handle icon button event
def icon_button_event():
    # Add code to handle the icon button click event
    pass

# Create a label for the listening post status
status_label = tk.Label(root, text="Listening Post Status: Not Running", bg=background_color)
status_label.pack(pady=10)

# Create a button to start the listening post
start_button = tk.Button(root, text="Start Listening Post", bg=secondary_color, fg=text_color, command=start_listening_post)
start_button.pack()

# 4. Incorporate Icons (Replace with your icon)
icon_image = tk.PhotoImage(file="C:/Users/noone/Desktop/Projects/C2/Misc/icon.png")
icon_button = tk.Button(root, image=icon_image, text="Icon Button", compound="left", bg=primary_color, fg=text_color, command=icon_button_event)
icon_button.image = icon_image  # Store a reference to the image
icon_button.pack(pady=20)

# Run the GUI application
root.mainloop()


