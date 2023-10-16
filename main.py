from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="INICIO")
@app.route("/tema1")
def tema1():
    return render_template("index.html", title="TEMA 1")

if __name__ == "__main__":
    app.run(debug=True)
