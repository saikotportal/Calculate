import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python_app'))

from flask import Flask, render_template, request, jsonify, session
from calculator import Calculator

app = Flask(__name__)
app.secret_key = "calculator-secret-key-2024"


def get_calculator(): 
    calc = Calculator()
    calc.history = session.get("history", [])
    return calc


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    operation = data.get("operation")

    if a is None or b is None or not operation:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid numbers"}), 400

    calc = get_calculator()

    ops = {
        "add": calc.add,
        "subtract": calc.subtract,
        "multiply": calc.multiply,
        "divide": calc.divide,
        "power": calc.power,
        "modulo": calc.modulo,
    }

    if operation not in ops:
        return jsonify({"error": "Unknown operation"}), 400

    try:
        result = ops[operation](a, b)
        session["history"] = calc.get_history()
        return jsonify({"result": result, "history": calc.get_history()})
    except ZeroDivisionError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/history", methods=["GET"])
def history():
    return jsonify({"history": session.get("history", [])})


@app.route("/history", methods=["DELETE"])
def clear_history():
    session["history"] = []
    return jsonify({"message": "History cleared"})


if __name__ == "__main__":
    app.run(debug=True)
