from flask import Flask, render_template, request, redirect
from main import solveDH

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bitlen = int(request.form['bitlen'])
        method = int(request.form['method'])
        if method:
            return redirect(f"/solve/{bitlen}/{method}")
    return render_template('index.jinja')

@app.route("/solve/<bitlen>/<method>", methods=["GET", "POST"])
def solve(bitlen, method):
    if request.method == 'POST':   
        return redirect("/") 
    dhc = solveDH(int(bitlen), int(method))
    results = dhc.getResults()
    return render_template("solve.jinja", results=results)

@app.errorhandler(400)
def badReqHandler(error):
    return render_template('index.jinja')