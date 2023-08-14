from flask import Flask, render_template, request
import tkinter as tk
from tkinter import ttk
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # debug
    #waitress.serve(app, host='0.0.0.0', port=7777)
