from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# TODO:
# Name the action for the form '/crossoff' and make its method 'post'.
# a form for crossing off watched movies
#<label for="watched-movie">           
#<input type="text" id="watched-movie" name="watched-#movie"/>  </label>
#{0}between select with get_current_watchlist():
crossoff_form = """
    <form action="/crossoff" method="post">
        <label>
            I want to cross off 
        <select name="watched-movie">
            <option>Star Wars</option> 
            <option>The Matrix</option>
        </select>
            from my watchlist.
            </label>
     <input type="submit" value="Cross It Off"/>
    </form>
"""

# TODO:
# Finish filling in the function below so that the user will see a message like:
# "Star Wars has been crossed off your watchlist".
# And create a route above the function definition to receive and handle the request from 
# your crossoff_form.
@app.route("/crossoff", methods=['POST']) 
def crossoff_movie():
    crossed_off_movie = request.form['watched-movie'] 

    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your Watchlist!"
    content = page_header + "<p>" + confirmation + "</p>" + page_footer

    return content 

# TODO:
# modify the crossoff_form above to use a dropdown (<select>) instead of
# an input text field (<input type="text"/>)




@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # build the response string
    content = page_header + edit_header + crossoff_form + page_footer

    return content


app.run()