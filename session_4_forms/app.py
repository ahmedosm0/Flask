from flask import Flask, render_template, redirect, url_for, flash
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_a_secret_key'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfuly Registered {form.username.data}!")
        return redirect(url_for('home'))
    return render_template('signup.html', title='signup', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    password = form.password.data
    print(f"email:{email} | pass:{password}")

    if form.validate_on_submit():  # when we pass hidden_tag() in html file only then it clicks
        print(f'validate_on_submit clicked')
        if email =='abc@y.z' and password == '12345':
            flash('Logged in Successfully!')
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password')

    return render_template('login.html', title='login', form=form)

if __name__=="__main__":
    app.run(debug=True)