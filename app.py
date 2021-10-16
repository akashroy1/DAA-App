from flask import Flask, request, render_template
from src import pattern_matching

app = Flask(__name__, template_folder='./src/template')

@app.route("/", methods= ['GET', 'POST'])
def home():
    # if(request.method == 'POST'):
    result1 = ''
    courseId = request.form.get("code", False) #'CSE2005'
    result1 = pattern_matching.find(courseId)
    return render_template("index.html", n = result1, cid = courseId)

app.run(debug=True)
