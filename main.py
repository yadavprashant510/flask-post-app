from flask import Flask, flash, redirect, render_template, url_for

from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '4e10bb420e7fe20190a0e99f35d55a25'
# dummy poste
posts = [
    {
        'author': 'Prashant Yadav',
        'title': 'Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 7, 2024',
    },
    {
        'author': 'Vishal Yadav',
        'title': 'Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 10, 2024',
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    else:
        print("Else exe")
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.email.data == 'admin@email.com' and form.password.data == 'password':
        flash("You have been logged in", 'success')
    else:
        flash("Login failed. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/contact')
def contact():
    return render_template('contact.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000,)
