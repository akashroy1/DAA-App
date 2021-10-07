from flask import Flask, render_template

app = Flask(__name__, template_folder='./src/template')

@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)
