from flask import Flask, request, redirect, render_template
import cgi
app = Flask(__name__)app.config['DEBUG'] = True

terrible_movies = [    
    "Gigli",    
    "Star Wars Episode 1: Attack of the Clones",
    "Paul Blart: Mall Cop 2",
    "Nine Lives",
    "Starship Troopers"
]

def get_watched_movies():
    #hard coded for now, list of crossed_off_movies: 
    return ["Iron man", "Cinderella", "Snow White", "Black Panther", "Spiderman"]

def get_current_watchlist():
    return [ "Star Wars", "Minions", "Freaky Friday", "My Favorite Martian" ]

@app.route("/", methods=['GET'])
def movie_ratings():     
    return render_template('ratings.html', watched_movies=get_watched_movies)

@app.route("/", methods=['POST'])
def rate_movie():
    rated_movie = request.form['rated-movie']
    movie_rating = request.form['movie-rating']
    return render_template('rating_confirmation.html', rated_movie=rated_movie)
    
@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']
    if crossed_off_movie not in get_current_watchlist():      
        error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)
        return redirect("/?error=" + error)    
    return render_template('crossoff.html', crossed_off_movie=crossed_off_movie)

@app.route("/add", methods=['POST'])
def add_movie():  
    new_movie = request.form['new-movie']
    if (not new_movie) or (new_movie.strip() == ""):     
        error = "Please specify the movie you want to add." 
        return redirect("/?error=" + error)    
    if new_movie in terrible_movies:   
        error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie)   
        return redirect("/?error=" + error)   
    return render_template('add-confirmation.html', movie=new_movie)

@app.route("/")
def index(): 
    encoded_error = request.args.get("error")    
    return render_template('edit.html', watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
