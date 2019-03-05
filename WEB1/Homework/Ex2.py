from flask import Flask,redirect
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, hihi"

list_name = [
    {
    "Name": "Quang",
    "Work": "learn about Python programming",
    "School": "TechKids",
    "Hobbies": ["walking", "sleeping", "picnic"],
    "My crush": ["Ngọc Trinh ^^", "Phương Trinh ^^"],
    },
    {
    "Name": "H",
    "Work": "work",
    "School": "School",
    "Hobbies": ["walking", "sleeping", "picnic"],
    "My crush": ["Ngọc Trinh ^^", "Phương Trinh ^^"],
    },
    {
    "Name": "D",
    "Work": "work",
    "School": "School1",
    "Hobbies": ["walking", "sleeping", "picnic"],
    "My crush": ["Ngọc Trinh ^^", "Phương Trinh ^^"],
    },
]

@app.route("/user/<username>")
def about_name(username):
    s = "User not found"
    for i in list_name:
        if username == i["Name"]:
            s = i
    return str(s)


if __name__ == '__main__':
  app.run(debug=True) 