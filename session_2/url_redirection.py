from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return f"<h1> welcome </h1>".title()

@app.route('/passed')
def passed():
    return f"<h1>congrats you are passed</h1>".title()

@app.route('/failed')
def failed():
    return f"<h1>sorry you are failed</h1>".title()

@app.route('/result/<name>/<int:num>')
def result(name, num):
    if num >= 45:
        return redirect(url_for('passed'))
    else:
        return redirect(url_for('failed'))

if __name__ == '__main__':
    app.run(debug=True)