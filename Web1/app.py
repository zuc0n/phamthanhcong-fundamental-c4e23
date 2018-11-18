from flask import Flask, render_template

app = Flask(__name__)

#function binding
@app.route('/')
def home():
    return "Hello Flask"


@app.route('/c4e')
def c4e():
    return "Hello c4e, hihi how are youd"


@app.route('/hi/<name>')
def hi(name):
    return "Hi " + name


@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    s = x + y
    return str(s)


@app.route('/posts/<int:index>')
def posts(index):
    titles = [
        "Troi mua to qua",
        "Troi nang to qua",
        "Troi lanh qua",
    ]
    contents = [
        "Toi di ngu",
        "Toi di an",
        "Toi di tam",
    ]
    t = titles[index]
    c = contents[index]
    return render_template('post.html', title=t, content=c)


@app.route('/movie')
def movie():
    return render_template('movie.html', name='Deadpool', image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhO_dGNJ0SRitJyYUWqI8gr6qOTFd6u6yPAE3VY9WgBujjcKPNWA")


@app.route('/movies')
def movies():
    # movie_titles = [
    #     "Superman",
    #     "Batman",
    #     "Dogman",
    #     "Catwoman",
    #     "Ironman",
    # ]
    movie_list =[
        {
            'title': 'Batman',
            'image': 'https://upload.wikimedia.org/wikipedia/en/thumb/1/17/Batman-BenAffleck.jpg/200px-Batman-BenAffleck.jpg',
        },
        {
            'title': 'Deadpool',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhO_dGNJ0SRitJyYUWqI8gr6qOTFd6u6yPAE3VY9WgBujjcKPNWA',    
        },
        {
            'title': 'Iroman',
            'image': 'https://www.sideshowtoy.com/assets/products/903341-iron-man-mark-iv/lg/marvel-iron-man-2-iron-man-mark-4-sixth-scale-figure-hot-toys-903340-08.jpg',
        }
    ]

    return render_template('movies.html', movies= movie_list)
if __name__ == '__main__':
    app.run(debug=True)