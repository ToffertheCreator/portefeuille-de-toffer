from flask import Flask, request, render_template, session
from algorithms import linked_list, stacks
import math, os

app = Flask(__name__)
app.secret_key = 'SDIYBT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/uppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofcircle():
    result=None
    if request.method == 'POST':
        inp_rad = request.form.get('inputnum', '')

        if inp_rad:
            rad = float(inp_rad)
            result = math.pi*(rad**2)
        else:
            result = "Missing Input"
    return render_template('areaofcircle.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    result=None
    if request.method == 'POST':
        str_base = request.form.get('inputbase', '')
        str_height = request.form.get('inputheight', '')
        
        if str_base and str_height:
            base = float(str_base)
            height = float(str_height)
            result = 0.5*base*height
        else:
            result = 'Missing Input'

    return render_template('areaoftriangle.html', result=result)

@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    message = ""
    removed_message = ""
    
    if request.method == 'GET':
        session['my_list_data'] = []
        session['message'] = ""
        session["removed_message"] = ""

    if 'my_list_data' not in session:
        session['my_list_data'] = []
    
    # Rebuild LinkedList from session data
    my_list = linked_list.LinkedList()
    for item in session['my_list_data']:
        my_list.insert_at_end(item)
    
    if request.method == 'POST':
        data = request.form.get('inputdata', '').strip()
        pos = request.form.get('index', type=int)
        operation = request.form.get('operation')

        if operation == 'insert_beginning' and data:
            my_list.insert_at_beginning(data)
        elif operation == 'insert_end' and data:
            my_list.insert_at_end(data)
        elif operation == 'insert_at' and data and pos is not None:
            my_list.insert_at(pos, data)
        elif operation == 'remove_beginning':
            remove_beginning = my_list.remove_at_beginning()
            removed_message = f"Data removed: {remove_beginning}"
        elif operation == 'remove_end':
            remove_end = my_list.remove_at_end()
            removed_message = f"Data remmoved: {remove_end}"
        elif operation == 'remove_at' and data is not None:
            remove_at = my_list.remove_at(data)
            removed_message = f"Data removed: {remove_at}"
        elif operation == 'search' and data:
            found = my_list.search(data)
            message = f"Data {'found at index 'f"{found[1]}" if found[0] else 'not found'} in the list"
        
        # Save list back to session
        session['my_list_data'] = my_list.display()
        session.modified = True
    else:
        message = session.get('message', '')
        message = session.get('message', '')
  
    list_items = my_list.display()
    return render_template('linkedlist.html', list_items=list_items, message=message, removed_message=removed_message)

@app.route('/contact')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)