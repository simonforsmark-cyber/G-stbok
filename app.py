python
from flask import Flask, request, render_template, redirect
from datetime import datetime

app = Flask(__name__)

FILE_PATH = "guestbook.txt"


@app.route("/")
def guestbook():
    posts = read_posts()
    return render_template("guestbook.html", posts=posts)


@app.route("/add", methods=["POST"])
def add_post():
    name = request.form.get("name")
    message = request.form.get("message")

    time = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"{name}|{time}|{message}\n")

    return redirect("/")


def read_posts():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
