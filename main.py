from flask import Flask, render_template, request

app = Flask(__name__)


def process_string(input_string):
    # Implement your logic to process the input string
    # For demonstration purposes, let's assume the processing is converting the string to uppercase
    processed_string = input_string.upper()
    return processed_string


@app.route("/", methods=["GET", "POST"])
def homepage():
    processed_string = None

    if request.method == "POST":
        input_string = request.form.get("input_string")
        processed_string = process_string(input_string)

    return render_template("index.html", title="Lenguajes y Automatas II", processed_string=processed_string)



if __name__ == "__main__":
    app.run(debug=True)
