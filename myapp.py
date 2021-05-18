from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        return "You have subscribed your phone number"


@app.route('/hello')
def hello_page():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
