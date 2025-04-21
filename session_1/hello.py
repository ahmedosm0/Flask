from flask import Flask

# WSGI (web server gateway interface)
app = Flask(__name__) # if we run this file, __name__ will considered as __main__, and the app will run, otherwise not run when using this as module from another file.

@app.route('/')
def welcome():
    return "<h1> welcome to flask! </h1>"

@app.route('/home')
def home():
    return "<h1>hello and welcome to the home page!</h1>"

@app.route('/square/<int:num>')
def square(num):
    return f"<h1>your number is {num} and it's square is {num*num}</h1>"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"<h1>{num1} + {num2} = {num1+num2}</h1>"

if __name__ == "__main__": # we use this coz to not run the app while importing this module in another file.
    app.run(debug=True)

print(f'this is hello module, with name: {__name__}') # when we run mod_1.py, it's class will be hello. but if we run hello.py, it's class will be "__main__"
