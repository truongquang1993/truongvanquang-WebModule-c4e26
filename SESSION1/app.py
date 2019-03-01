from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello C4E, this is home page Hihi"

if  __name__ == "__main__":
    app.run(debug=True)
