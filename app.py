from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "asbhkanjnbhjk"


@app.route("/hello")
def index():
    flash("what is your name?")
    return render_template("index.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input'] + "."))
    return render_template("index.html")
