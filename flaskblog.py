from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from os import environ
app = Flask(__name__)

app.config['SECRET_KEY'] = '16dd91dd0b8189950f260d479dd9cbe7'

posts = [
    {
        'author'    :   'Cory Schafer',
        'title'     :   'Blog Post 1',
        'C=content'   :   'First Post Content',
        'date_posted'   :   'April 16, 2023',
    },
    {
        'author'    :   'Jane Doe',
        'title'     :   'Blog Post 2',
        'C=content'   :   'Second Post Content',
        'date_posted'   :   'April 15, 2023',
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)