from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, hihi"


@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    n = 0.01*height
    BMI = weight/(n*n)

    if  BMI < 16:
        s = "Severely underweight"
    elif BMI < 18.5:
        s = "Underweight" 
    elif BMI < 25:
        s = "Normal"
    elif BMI < 30:
        s = "Overweight"
    else:
        s = "Obese"
    return s



if __name__ == '__main__':
  app.run(debug=True) 