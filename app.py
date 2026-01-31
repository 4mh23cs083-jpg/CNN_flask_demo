import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/abc")
def abc():
    return render_template("abc.html")

@app.route("/luffy")
def luffy():
    return render_template("image.html", title="Monkey D. Luffy", image_file="luffy.png")

@app.route("/sanji")
def sanji():
    return render_template("image.html", title="Sanji", image_file="sanji.png")

@app.route("/zoro")
def zoro():
    return render_template("image.html", title="Roronoa Zoro", image_file="zoro.png")

@app.route("/<name>")
def index(name):
    return render_template("name.html", name=name)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
