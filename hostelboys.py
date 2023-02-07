from flask import Flask, render_template, request
app = Flask(__name__)

movies = [
    {'title': 'Puss In Boots (2022)', 'url': 'https://yts.mx/movies/puss-in-boots-the-last-wish-2022'},
    {'title': 'The Bubble (2022)', 'url': 'https://yts.mx/movies/the-bubble-2022'},
    {'title': 'Kubo and the Two Strings (2016)', 'url': 'https://yts.mx/movies/kubo-and-the-two-strings-2016'},
    {'title': 'Project wolf hunting (2022)', 'url': 'https://yts.mx/movies/project-wolf-hunting-2022'},
    {'title': 'Assasins Creed (2022)', 'url': ''},
    {'title': 'Hunting Souls (2022)', 'url': 'https://yts.mx/movies/hunting-souls-2022'}
]

@app.route('/')
def index():
    return render_template('index.html', movies=movies)

@app.route('/watch/<int:id>')
def watch(id):
    try:
        movie = movies[id]
    except IndexError:
        return "Movie not found",404
    return render_template('watch.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
