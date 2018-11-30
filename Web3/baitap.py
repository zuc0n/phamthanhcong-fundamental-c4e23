from flask import Flask, render_template, request
import mlab
from movies import Register

baitap = Flask(__name__)
mlab.connect()

@baitap.route("/new_member", methods=["GET", "POST"])
def new_member():
    if request.method == "GET":
        return render_template("new_member.html")
    elif request.method == "POST":
        form = request.form 
        u = form["username"]
        p = form["password"]
        exist_user = User.objects(username=u).first()
        if exist_user !=None: #Found existing user
            return "User already existed"
        else:
            r = Register(username= u, password= p)
            r.save()
            return "Welcome"
if __name__ == "__main__":
    baitap.run(debug=True)