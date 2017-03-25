from flask import *
import mlab
from models.CarItems import CarItems


app = Flask(__name__)


#connect to mlab database
mlab.connect()

#create a new CarItems and save it to database
# new_car = CarItems()
# new_car.src = "http://st.motortrend.com/uploads/sites/5/2012/12/2014-BMW-M6-Gran-Coupe-rear-three-quarters.jpg"
# new_car.title = "Item 2"
# new_car.description = "Description for Item 2"
# new_car.save()



@app.route('/')
def hello_world():
    return redirect(url_for("foodblog"))


@app.route('/addcars', methods=["GET", "POST"])
def add_cars():
    if request.method == "GET":
        return render_template("addcars.html")
    if request.method == "POST":
        new_car = CarItems()
        new_car.src = request.form["source"]
        new_car.title = request.form["title"]
        new_car.image = request.f("image")
        new_car.description = request.form["description"]
        new_car.save()
        return render_template("addcars.html")


@app.route('/deletecars', methods=["GET", "POST"])
def delete_cars():
    if request.method == "GET":
        return render_template("deletecars.html")
    if request.method == "POST":
        new_car = CarItems.objects(title=request.form["title"]).first()
        if new_car is not None:
            new_car.delete()
        return render_template("deletecars.html")

@app.route('/updatefood')

@app.route('/foodblog')
def foodblog():
    return render_template("foodblog.html", car_items=CarItems.objects())

if __name__ == '__main__':
    app.run()
