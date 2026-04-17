from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['username']
    return f"Hello {name}"

app.run(debug=True)