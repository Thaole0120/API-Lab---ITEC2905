# import Flask - framework we are using for our website
from flask import Flask, render_template

# create a new Flask app
app = Flask(__name__)

# Create route for the home page ( index.html )
@app.route('/')

# Create the index method - this method is going to assign the API key for the map on the home page 
# and render the home page
def index():
    # Using instructor-provided API key
    api_key = "AIzaSyCdtcEmCii8bNySWzGtpwwWmwBDjp2nKi4"
    return render_template('index.html', api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)