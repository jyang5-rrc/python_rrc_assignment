from flask import Flask, render_template, request
from challenge4c_math import MyMath

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num_list = [float(num) for num in request.form['num1'].split()]
    num_list = tuple(num_list)
    operator = request.form['operator']
    
    my_math = MyMath(*num_list)
    operator1 =''
    result =''
    
    if operator == 'max':
        result = my_math.max()
        operator1 = 'Maximum'
    elif operator == 'avg':
        result = my_math.avg()
        operator1 = 'Average'
    elif operator == 'stdDev':
        result = my_math.stdDev()
        operator1 = 'Standard Deviation'
    elif operator == 'all':
        result = {}
        result['max'] = my_math.max()
        result['avg'] = my_math.avg()
        result['stdDev'] = my_math.stdDev()
        operator1 = 'All'
        
    
    return render_template('page.html', num_list=num_list, operator=operator1, result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
