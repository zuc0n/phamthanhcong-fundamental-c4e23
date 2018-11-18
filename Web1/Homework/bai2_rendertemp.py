from flask import *

app = Flask(__name__)
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    s = weight/((height/100)*2)
    if s < 16:
        anw = 'Severely underweight'
    elif s >= 16 and s < 18.5:
        anw = 'Under weight'
    elif s >= 18.5 and s < 25:
        anw = 'Normal'
    elif s >= 25 and s < 30:
        anw = 'Overweight'
    elif s > 30:
        anw = 'Obese'
    return render_template('bmi.html', anw= anw)




if __name__ == '__main__':
    app.run(debug=True)