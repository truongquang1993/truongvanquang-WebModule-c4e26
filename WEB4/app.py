from flask import Flask, render_template, request
from db import food_collection
from db1 import user_collection
from bson import ObjectId
import food

app = Flask(__name__)


@app.route("/food_list")
def food_list():
    all_food = food.get({})
    return render_template("food_list.html", f_list=all_food)

@app.route("/food/<id>", methods=["GET", "POST"])
def food_detail(id):
    if request.method == "GET":
        f = food.get_by_id(id)
        return render_template("detail_food.html", f_list=f)
    elif request.method == "POST":
        food.del_by_id(id)
        all_food = food.get({})
        return render_template("food_list.html", f_list=all_food)

@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("new_food.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        price = form["price"]
        food.add_new_food(name, price)
        all_food = food.get({})
        return render_template("food_list.html", f_list=all_food)

@app.route("/user/add", methods=["GET","POST"])
def add_user():
    if request.method=="GET":
        return render_template("add_user.html")
    elif request.method=="POST":
        form=request.form
        user=form["username"]
        pas=form["password"]
        new_user={
            "username":user,
            "password":pas,
        }
        user_collection.insert_one(new_user)
        return "New user added"
        
@app.route("/user", methods=["GET","POST"])
def user():
    if request.method=="GET":
        return render_template("user.html")
    elif request.method=="POST":
        form=request.form
        user=form["username"]
        users={
            "username":user,
        }
        a=user_collection.find(
            {
            "user": users["username"]
            }
        )
        if a ==None:
            return "This user doesn't exist. Please register a new account"
        else:
            return "User name already in use"

if __name__ == '__main__':
  app.run(debug=True)