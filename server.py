"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
INSULT = ["You must have been born on a highway, because that's where most accidents happen.",
"Shut up, you'll never be the man your mother is.",
"It looks like your face caught on fire and someone tried to put it out with a fork.",
"Your family tree is a cactus, because everyone on it is a prick."]


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page. 
    <br>
    Click <a href="/hello"> hello</a> to get to the next page </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name and compliment them"""

    return """
    <!doctype html> 
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Select a compliment:
          <select name = "compliment">
           <option value = "awesome"> Awesome</option>
            <option value = "terrific"> Terrific </option>
            <option value = "fantastic"> Fantastic</option>
            <option value = "coolio"> Coolio</option>
            <option value = "Wowza"> Wowza </option>
            <option value = "Neato"> Neato</option>
           
            
          <input type="submit" value="Submit">
        <br><br>
        </form>

        <form action="/diss">
        
          Select a diss:
         <input type = "submit" value = "submit">
          
          
        </form>
      </body>
    </html>
    """




@app.route('/greet')
def greet_person():
    """Get user by name and compliment."""

    player = request.args.get("person")

    compliment =request.args.get("compliment")

    

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Diss the user."""

    #player = request.args.get("person")
    insult = choice(INSULT)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
         {insult}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
