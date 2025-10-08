from flask import Flask, redirect, url_for, request, render_template, flash
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

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
        inp = float(request.form.get('inputnum', 0))
        result = math.pi*(inp**2)
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

@app.route('/contact')
def contact():
    return "Contact Page. please create me an html page with dummy contact info"

if __name__ == "__main__":
    app.run(debug=True)
