from flask import Flask, render_template, url_for
from employes_db import employees_data

app = Flask(__name__)

@app.route('/')
def welcome():
    return f"<h1> Welcome </h1>"

@app.route('/home')
def home():
    return render_template('home.html', title = 'homepage')

@app.route('/about')
def about():
    return render_template('about.html', title = 'aboutpage')

@app.route('/check/<int:num>')
def check(num):
    return render_template('check.html', title = 'checking', number = num)

@app.route('/employes')
def employes():
    return render_template('employes.html', title = 'employes', empdb = employees_data)

@app.route('/employes/<role>')
def employes_roles(role):
    return render_template('employes_roles.html', title = 'employes roles', role = role, empdb = employees_data)

if __name__ == "__main__":
    app.run(debug=True)