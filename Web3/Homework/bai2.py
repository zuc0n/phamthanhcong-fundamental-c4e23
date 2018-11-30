from flask import Flask, render_template, request
import mlab
from movies import Bike

app = Flask(__name__)

mlab.connect()
@app.route("/bike_rental", methods=["GET","POST"] )
def bike_rental():
    if request.method == "GET":
        # User request form
        return render_template("bike_rental.html")
    elif request.method == "POST":
        form = request.form 
        m = form["model"]
        i = form["image"]
        y = form["year"]
        f = form["fee"]
        m = Bike(model= m, image= i, year= y, fee= f)
        m.save()
        return "Gotcha!!!!"

if __name__ == "__main__":
    app.run(debug=True)