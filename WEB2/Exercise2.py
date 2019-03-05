from flask import Flask, render_template, request
app = Flask(__name__)

vehicle_list = [
    {
        "Model": "Yamaha",
        "Daily fee (VND)": 125000,
        "Image": "https://yamaha-motor.com.vn/wp/wp-content/uploads/2018/07/500x400-8.png",
        "Year": 2018,
    },
]

@app.route("/")
def menu():
    return render_template("menu_bike.html", vehicle_list=vehicle_list)

@app.route("/new_bike", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
        form = request.form
        model = form["Model"]
        daily_fee = form["Daily fee"]
        image = form["Image"]
        year = form["Year"]
        new_vehicle = {
            "Model": model,
            "Daily fee": daily_fee,
            "Image": image,
            "Year": year,
        }
        vehicle_list.append(new_vehicle)
        return str(vehicle_list)

if __name__ == '__main__':
  app.run(debug=True)