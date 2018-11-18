from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/school')
def school():
    return redirect('http://techkids.vn ')

@app.route('/about-me')
def about_me():
    return render_template("about-me.html")

if __name__ == '__main__':
    app.run(debug=True)