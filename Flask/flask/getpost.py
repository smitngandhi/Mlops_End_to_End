'''Testing Render Template'''
from flask import Flask , render_template , request

'''Creating WSGI (Web Server Gateway Interface)'''
app = Flask(__name__)

# Default route
@app.route("/")
def welcome():
    return "Hello User, Welcome to the app"


@app.route("/index" , methods=['GET'])
def index():
    # It will search for index.html in the same folder or in the templates folder in the same directory
    return render_template('index.html')

@app.route("/aboutus")
def about():
    return render_template('aboutus.html')


@app.route('/form' , methods=['GET' , 'POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Hello {name}. Your entered mail is {email} and message is {message}"
    return render_template('form.html')

@app.route('/submit' , methods=['GET' , 'POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Hello {name}. Your entered mail is {email} and message is {message}"
    return render_template('form.html')



if __name__ == "__main__":
    # By writing debug=True we can watch the live changes on the web app
    app.run(debug=True)
