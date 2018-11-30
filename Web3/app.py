from flask import Flask, render_template, request
import mlab
from movies import Movie

app = Flask(__name__)

mlab.connect()
@app.route("/add_movie", methods=["GET","POST"] )
def add_movie():
    if request.method == "GET":
        # User request form
        return render_template("add_movie.html")
    elif request.method == "POST":
        form = request.form 
        t = form["title"]
        i = form["image"]
        y = form["year"]
        
        m = Movie(title= t, image= i, year= y)
        m.save()
        return "Gotcha!!!!"

if __name__ == "__main__":
    app.run(debug=True)