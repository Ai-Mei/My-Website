from flask import Flask, render_template, request
from merge_and_sort import connect_linked_lists, sort_linked_list, create_linked_list

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


@app.route('/merge_and_sort', methods=['GET', 'POST'])
def merge_and_Sort():
    result = ''
    error_message = ''
    if request.method == 'POST':
        list1_values = request.form.get('list1_values', '')
        list2_values = request.form.get('list2_values', '')
        if not isinstance(list1_values, str) or not isinstance(list2_values, str):
            error_message = "Invalid input. Please provide valid values."
            return render_template('merge_and_sort.html', result='', error_message=error_message)
        # Create linked lists or handle the error
        list1 = create_linked_list(list1_values)
        list2 = create_linked_list(list2_values)
        if isinstance(list1, str) or isinstance(list2, str):
            error_message = list1 if isinstance(list1, str) else list2
            return render_template('merge_and_sort.html', result='', error_message=error_message)
        connected_list = connect_linked_lists(list1, list2)
        sorted_list = sort_linked_list(connected_list)
        sorted_list_str = ""
        while sorted_list is not None:
            sorted_list_str += str(sorted_list.value) + " "
            sorted_list = sorted_list.next
        result = sorted_list_str.strip()
    return render_template('merge_and_sort.html', result=result, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)



