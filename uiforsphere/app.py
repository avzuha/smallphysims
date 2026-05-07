from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

epsilon0 = 8.854e-12

def electric_field(r, R, q):
    k = 1 / (4 * np.pi * epsilon0)
    if r < R:
        return k * q * r / R**3
    elif abs(r - R) < 1e-6:
        return k * q / R**2
    else:
        return k * q / r**2

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    x = float(data["x"])
    y = float(data["y"])
    R = float(data["R"])
    q = float(data["q"])

    r = np.sqrt(x**2 + y**2)
    E = electric_field(r, R, q)

    return jsonify({
        "x": round(x, 2),
        "y": round(y, 2),
        "r": round(r, 2),
        "E": "{:.3e}".format(E)
    })

@app.route("/graph", methods=["POST"])
def graph():
    data = request.get_json()
    R = float(data["R"])
    q = float(data["q"])

    r_vals = np.linspace(0.01, 2*R, 200)
    E_vals = [electric_field(rv, R, q) for rv in r_vals]

    return jsonify({
        "r": [round(float(rv), 2) for rv in r_vals],
        "E": E_vals
    })

if __name__ == "__main__":
    app.run(debug=True)