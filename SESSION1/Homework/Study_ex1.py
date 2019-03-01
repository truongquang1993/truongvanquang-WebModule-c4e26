from flask import Flask
from flask import Flask,redirect
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, hihi"

me = {
    "Name": "mr. Quang",
    "Work": "learn about Python programming",
    "School": "TechKids",
    "Hobbies": ["walking", "sleeping", "picnic"],
    "My crush": ["Ngọc Trinh ^^", "Phương Trinh ^^"],
}

@app.route("/about-me")
def about_me():
    return str(me)


@app.route("/school")
def school():
    return redirect("http://techkids.vn/")


if __name__ == '__main__':
  app.run(debug=True) 