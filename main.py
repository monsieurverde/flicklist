from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = ""
    movie2 = ""

    movie = get_random_movie()
    movie2 = get_random_movie()
    if movie2 == movie:
        movie2 = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    content += "<h1>Tomorrows Movie</h1>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
   
    movies = {1: "StarWars", 2: "Aliens", 3: "GGG", 4: "Predator", 5: "Intersteller"}
    z = len(movies.keys())
    x = random.randint(1,z)
   
    return movies[x]


app.run()