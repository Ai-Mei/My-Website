from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    result = None
    if request.method == 'POST':
        radius = float(request.form.get('inputRadius', ''))
        result = 3.14*(radius**2)
    return render_template('areaOfcircle.html', result=result)

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def areaOftriangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('inputbase', ''))
        height = float(request.form.get('inputheight', ''))
        result = base*height
    return render_template('areaOftriangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)



