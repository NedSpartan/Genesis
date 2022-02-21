from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/onboarding")
def onboarding():
    return render_template("onboarding.html", title="Onboarding")

@app.route("/upcomingevents")
def upcomingevents():
    return render_template("upcomingevents.html", title="Upcoming Events")

@app.route("/test")
def test():
    return render_template("layout.html", title="test")

app.route("/guides")
def guides():
    return render_template("guides.html", title="Guides")

app.route("/tools")
def guides():
    return render_template("guides.html", title="Tools")

app.route("/guides")
def guides():
    return render_template("fits.html", title="Fits")

@app.route("/r")
def rolling():
    return render_template("rolling.html", title="Rolling Guide")