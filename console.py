from pystyle import Colors, Colorate
from pystyle import Anime, Center
from os import system
import time
from pystyle import Colors, Colorate
from rich.progress import track
from flask import Flask, request, render_template
import tkinter as tk
import sys
import random
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import filedialog


def process_command(command):
    if command.lower() == "hello":
        return "welcome to cloudconsole v1.0!"
    elif command.lower().startswith("say "):
        return command[4:]
    elif command.lower() == "help":
        return """commands:
    say <text> - type your text
    clear - clear the console
    help - display list of commands
    info - display info"""
    elif command.lower() == "clear":
        return "console cleared."
    elif command.lower() == "info":
        return """made by toxinsfx
    (made in python)
    """
    else:
        return "command not recognized."
    
def enter_text():
    input_text = input_entry.get()
    console_text.config(state="normal")
    console_text.insert("end", f"> {input_text}\n", "user")

    response = process_command(input_text)
    console_text.insert("end", f"{response}\n", "response")

    console_text.see("end")
    console_text.config(state="disabled")
    input_entry.delete(0, "end")


    
# Create the main window
root = tk.Tk()
root.title("Console V1.0")

 # Set the dimensions of the window
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

 # Create a frame on the left for the menu
menu_frame = tk.Frame(root, bg="light gray")
menu_frame.pack(side="left", fill="y")

 # Create buttons in the menu frame
settings_button = tk.Button(menu_frame, text="Settings")
settings_button.pack(padx=10, pady=10, anchor="w")

console_button = tk.Button(menu_frame, text="Console")
console_button.pack(padx=10, pady=10, anchor="w")

 # Create a frame on the right for the console
console_frame = tk.Frame(root)
console_frame.pack(side="right", fill="both", expand=True)

 # Create a simple console-like textbox
console_text = tk.Text(console_frame, wrap=tk.WORD, state="disabled")
console_text.tag_config("user", foreground="blue")
console_text.tag_config("response", foreground="green")
console_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

 # Add initial message
initial_message = "Type 'help' to get a list of commands\n"
console_text.config(state="normal")
console_text.insert("end", initial_message, "initial")
console_text.config(state="disabled")

 # Create an entry for input
input_entry = tk.Entry(console_frame)
input_entry.pack(side="bottom", fill="x", padx=20, pady=10)

 # Create a button with "Enter" text
button = tk.Button(console_frame, text="Enter", command=enter_text, width=10, height=2)
button.pack(side="bottom", padx=20, pady=10)

 # Start the GUI event loop
root.mainloop()
    
    



















