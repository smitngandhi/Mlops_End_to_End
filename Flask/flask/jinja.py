'''Testing Render Template'''
from flask import Flask , render_template , request , redirect , url_for

'''Creating WSGI (Web Server Gateway Interface)'''

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''


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



# @app.route('/submit' , methods=['GET' , 'POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#         return f"Hello {name}. Your entered mail is {email} and message is {message}"
#     return render_template('form.html')

@app.route('/submit' , methods=['GET' , 'POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Hello {name}. Your entered mail is {email} and message is {message}"
    return render_template('marks.html')

# Variable rule
@app.route('/success/<float:score>')
def score(score):
    res = ""
    if score>20:
        res = "PASS"
    else:
        res = "FAIL"

    return render_template('result.html' , results = res )


@app.route('/submit_marks' , methods=['GET' , 'POST'])
def submit_marks():
    average = 0
    if request.method=='POST':
        sub1 = float(request.form['subject1'])
        sub2 = float(request.form['subject2'])
        sub3 = float(request.form['subject3'])

    average = (sub1 + sub2 + sub3) /3

    return redirect(url_for('score' , score=average))


if __name__ == "__main__":
    # By writing debug=True we can watch the live changes on the web app
    app.run(debug=True)
