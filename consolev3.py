import tkinter as tk
from flask import Flask, render_template, request
import waitress

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        response = process_command(input_text)
        return render_template('index.html', response=response)
    return render_template('index.html')

def launch_web_version():
    waitress.serve(app, host="0.0.0.0", port=7777)

def enter_text(console_text, input_entry):
    input_text = input_entry.get()
    console_text.config(state="normal")
    console_text.insert("end", f"> {input_text}\n", "user")

    response = process_command(input_text)
    console_text.insert("end", f"{response}\n", "response")

    console_text.see("end")
    console_text.config(state="disabled")
    input_entry.delete(0, "end")

def launch_gui_version():
    root = tk.Tk()
    root.title("cloud console")

    # Set the dimensions of the window
    window_width = 800
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    # Create a frame on the left for the menu
    menu_frame = tk.Frame(root, bg="light gray")
    menu_frame.pack(side="left", fill="y")

    # Create buttons in the menu frame
    settings_button = tk.Button(menu_frame, text="settings")
    settings_button.pack(padx=10, pady=10, anchor="w")

    console_button = tk.Button(menu_frame, text="console")
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
    initial_message = "type 'help' to get a list of commands\n"
    console_text.config(state="normal")
    console_text.insert("end", initial_message, "initial")
    console_text.config(state="disabled")

    # Create an entry for input
    input_entry = tk.Entry(console_frame)
    input_entry.pack(side="bottom", fill="x", padx=20, pady=10)

    # Create a button with "enter" text
    button = tk.Button(console_frame, text="enter", command=lambda: enter_text(console_text, input_entry), width=10, height=2)
    button.pack(side="bottom", padx=20, pady=10)

    root.mainloop()

def main():
    choice = input("what version should i launch (web/gui): ").strip().lower()
    if choice == 'web':
        launch_web_version()
    elif choice == 'gui':
        launch_gui_version()
    else:
        print("invalid choice. please enter 'web' or 'gui'.")

if __name__ == '__main__':
    main()
