from flask import Flask
app = Flask(__name__)
# Bind route to view function
@app.route("/") #"/": Dịnh nghĩa là trang chủ
def home():# chịu trách nhiệm về hiển thị
    return "Hello, hihi"

@app.route("/myclass")
def myclass():
    return "C4E26, Son, Tuan ..."

@app.route("/hi/<name>")
def hiduc(name):
    return "Hi " + name

@app.route("/add/<nbr1>/<nbr2>")
def hi(nbr1, nbr2):
    add = int(nbr1) + int(nbr2)
    return str(add)

# Một cách khác khi buộc nhập vào là int
# @app.route("/add/<int:nbr1>/<int:nbr2>")
# def hi(nbr1, nbr2):
#     add = nbr1 + nbr2
#     return str(add)
food_menu = ["Cơm", "Phở bò", "Cơm rang"]

@app.route("/menu")
def menu():
    return str(food_menu)

@app.route("/food/<int:nbr>")
def food(nbr):
    return food_menu[nbr]

if __name__ == '__main__':
  app.run(debug=True)