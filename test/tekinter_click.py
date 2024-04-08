import tkinter as tk
import time

def on_click(event):
    global last_click_time
    click_time = time.time()

    # If time since last click is less than 0.3 seconds, it's a double click
    if (click_time - last_click_time) < 0.3:
        print("Double Click Detected!")
    else:
        # This is where you handle a single click event
        print("Single Click")

    # Update the last click time
    last_click_time = click_time

# Initialize the last click time
last_click_time = 0

# Set up the GUI
root = tk.Tk()
frame = tk.Frame(root, width=100, height=100)
frame.bind("<Button-1>", on_click)
frame.pack()

root.mainloop()

