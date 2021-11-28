from flask import Flask, render_template, request
from main import solveDH

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        bitlen = int(request.form['bitlen'])
        method = int(request.form['method'])
        print(bitlen, method)
        if method:
            return solve(bitlen, method)
        return render_template('index.jinja')
    else:
        return render_template('index.jinja')

@app.route("/solve", methods=["GET", "POST"])
def solve(bitlen, method):
    dhc = solveDH(bitlen, method)
    results = dhc.getResults()
    return render_template("solve.jinja", results=results)

@app.errorhandler(400)
def badReqHandler(error):
    return render_template('index.jinja')