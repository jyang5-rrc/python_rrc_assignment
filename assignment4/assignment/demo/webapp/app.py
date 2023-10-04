from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')#this determines the entry point; the / means the root of the website, so https://127.0.0.1:5000/
def index():#this is the name you give the route, in this case index, because it’s the index (or homepage) of the website
     return render_template('index.html')#this is the content of the web page,

@app.route('/cakes')
def cakes():
    return render_template('cake.html')

@app.route('/hello/<name>')#the <name> part means it passes the name into the hello function as a variable called name.
def hello(name):#this is the function that determines what content is shown. Here, the function takes the given name as a parameter.
    return render_template('page.html', name=name)#this code looks up the template page.html and passes in the variable name from the URL so that the template can use it.

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')#the host='0.0.0.0' means the web app is accessible to any device on the network.

