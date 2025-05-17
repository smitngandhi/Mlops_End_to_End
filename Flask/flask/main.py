'''Testing Render Template'''
from flask import Flask , render_template

'''Creating WSGI (Web Server Gateway Interface)'''
app = Flask(__name__)

# Default route
@app.route("/")
def welcome():
    return "Hello User, Welcome to the app"


@app.route("/index")
def index():
    # It will search for index.html in the same folder or in the templates folder in the same directory
    return render_template('index.html')

@app.route("/aboutus")
def about():
    return render_template('aboutus.html')


if __name__ == "__main__":
    # By writing debug=True we can watch the live changes on the web app
    app.run(debug=True)
