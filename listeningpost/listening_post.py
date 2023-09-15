import tkinter as tk

# Define the IP address and port for the listening post
LISTENING_IP = '0.0.0.0'
LISTENING_PORT = 8081

# Create the main application window
root = tk.Tk()
root.title("Concussion C2 Listening Post")
root.geometry("400x300")  # Adjust the window size as needed

# 1. Use a Consistent Color Scheme
primary_color = "#3498db"
secondary_color = "#2ecc71"
background_color = "#f2f2f2"
text_color = "#333333"

root.configure(bg=background_color)

# 2. Add Labels and Headings
main_heading = tk.Label(root, text="Concussion C2 Listening Post", font=("Helvetica", 16, "bold"), bg=primary_color, fg=text_color)
main_heading.pack(pady=(20, 10))

# Create a label for the listening post status
status_label = tk.Label(root, text="Listening Post Status: Running", bg=background_color)
status_label.pack(pady=10)

# 3. Improve Button Styling
start_button = tk.Button(root, text="Start Listening", bg=secondary_color, fg=text_color, command=start_listening)
start_button.pack()

# Placeholder for the start_listening function
def start_listening():
    # Placeholder for listening post start logic
    status_label.config(text="Listening Post Status: Listening")

# 4. Enhance Entry Fields
command_entry = tk.Entry(root, width=40, font=("Helvetica", 12), bg="#ffffff")
command_entry.pack()

# 5. Incorporate Icons (Replace with your icon path)
icon_image = tk.PhotoImage(file="C:/Users/noone/Desktop/Projects/C2/Misc/icon.png")
icon_button = tk.Button(root, image=icon_image, text="Icon Button", compound="left", bg=primary_color, fg=text_color, command=icon_button_event)
icon_button.image = icon_image  # Store a reference to the image
icon_button.pack(pady=20)

# Placeholder for the icon_button_event function
def icon_button_event():
    # Add code to handle the icon button click event
    pass

# Run the GUI application
root.mainloop()

