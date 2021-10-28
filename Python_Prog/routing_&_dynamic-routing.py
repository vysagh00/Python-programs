from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

# @app.route("/")
# def hi():
#     return"hello world"

# @app.route("/pops")
# def greet():
#     return"hello pops"

@app.route("/jp")
def oops():
    return"<h1 style=\"color:red\">focil kio</h1>"


@app.route("/img")
def pic():
    return render_template("index.html")    

@app.route("/<name>")
def peru(name):
    # return "hello " +  name
    return "hello " +  name.capitalize()     

if __name__== "__main__":
    app.run(debug=True, port=8000)