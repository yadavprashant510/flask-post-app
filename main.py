from flask import Flask, render_template

app = Flask(__name__)

# dummy post
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


@app.route('/contact')
def contact():
    return render_template('contact.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000,)
