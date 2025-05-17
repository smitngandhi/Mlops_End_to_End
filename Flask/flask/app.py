from flask import Flask

'''Creating WSGI (Web Server Gateway Interface)'''
app = Flask(__name__)

# Default route
@app.route("/")
def welcome():
    return "Hello Moto. FY"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__ == "__main__":
    # By writing debug=True we can watch the live changes on the web app
    app.run(debug=True)
