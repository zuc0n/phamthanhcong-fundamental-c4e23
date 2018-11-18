from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def user_name(username):
    users = {
        'user_a' : {
            'Name': 'Cris Pham',
            'Age': 22,
        },
        'user_b' : {
            'Name': 'Mymy',
            'Age': 21,
        },
        'user_c': {
            'Name': 'ChangLinh',
            'Age': 20,
        }
    }
    if username in users:
        u = users[username]
        return render_template('option.html',name= u['Name'], age= u['Age'])
    else:
        return 'User not found'


if __name__ == '__main__':
    app.run(debug=True)