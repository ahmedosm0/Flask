from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return f"<h1>welcome</h1>".title() # .title() capatilize first alphabet of word.

@app.route('/home/<name>/<marks>')
def student_marks(name, marks):
    return f"<h1>congrats {name} you got {marks} marks</h1>".title() 

if __name__=="__main__":
    app.run(debug=True)