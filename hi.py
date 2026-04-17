from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO TOH KAISA HA APP LOG !"

@app.route("/about")
def about():
    return "This is About Page"

if __name__ == "__main__":
    app.run(debug=True)