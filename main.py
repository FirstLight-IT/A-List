from Website import create_app
from flask import render_template, request

app = create_app()

@app.route('/')
def default():
    return "<h1>WELCOME TO IASite</h1>"

@app.route('/login')
def login():
    return render_template('ias_signup.html')


if __name__ ==  '__main__':
    app.run(debug=True)   