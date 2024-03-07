# Put your app in here.

from flask import Flask, request

from operations import add,sub,div,mult

app = Flask(__name__)

@app.route("/add")
def add_par():
    """Add a and b"""
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= add(a,b)
    return str(result)

@app.route("/sub")
def sub_par():
    """Subtract a and b"""
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route("/div")
def div_par():
    """Divide a and b"""
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result = div(a,b)
    return str(result)

@app.route("/mult")
def mult_par():
    """Multiply a and b"""
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result = mult(a,b)
    return str(result)



operators = {
    "add":add,
    "sub":sub,
    "div":div,
    "mult":mult
    }

@app.route("/math/<op>")
def do_math(op):
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    result= operators[op](a,b)
    return str(result)


