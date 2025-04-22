from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>welcome</h1>".title()

@app.route('/passed/<sname>/<int:num>')
def passed(sname, num):
    return f"<h1> congrats {sname} you are passed your obtained marks are {num} </h1>".title()

@app.route('/failed/<sname>/<int:num>')
def failed(sname, num):
    return f"<h1> sorry {sname} you are failed your obtained marks are {num} </h1>".title()

@app.route('/score/<name>/<int:marks>')
def score(name, marks):
    if marks>=45:
        return redirect(url_for("passed", sname = name, num = marks))
    else:
        return redirect(url_for("failed", sname = name, num = marks))


if __name__ == "__main__":
    app.run(debug=True)