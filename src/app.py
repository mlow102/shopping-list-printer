# Runs the shopping list web app, summons the print script, and handles the shopping list

from flask import Flask, render_template, request, redirect
import subprocess
app = Flask(__name__)
shopping_list = []

def save_shopping_list():
    with open('shopping_list.txt', 'w') as file:
        file.write('\n'.join(shopping_list))

def load_shopping_list():
    try:
        with open('shopping_list.txt', 'r') as file:
            return [item.strip() for item in file.readlines()]
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    global shopping_list
    shopping_list = load_shopping_list()
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add', methods=['POST'])
def add():
    item = request.form['item']
    shopping_list.append(item)
    save_shopping_list()
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
    item = request.form['item']
    if item in shopping_list:
        shopping_list.remove(item)
        save_shopping_list()
    return redirect('/')

@app.route('/print', methods=['POST'])
def print_shopping_list():
    # Save the shopping list to a temporary file
    temp_file = 'temp_shopping_list.txt'
    with open(temp_file, 'w') as file:
        file.write('\n'.join(shopping_list))

    # Call the external Python script to print the shopping list
    script_path = 'print.py'
    subprocess.run(['python', script_path, temp_file])

    return redirect('/')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True) 
