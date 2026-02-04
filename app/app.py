from flask import Flask, render_template, request

app = Flask(__name__)
score = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global score
    if request.method == "POST":
        score += 1
    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
