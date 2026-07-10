from flask import Flask, jsonify, request

from auth import login, SECRET_KEY
from admin import ping_host, read_log, calculate

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route("/")
def index():
    return jsonify({"service": "code-assist-demo", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/login", methods=["POST"])
def login_route():
    username = request.form["username"]
    password = request.form["password"]
    user = login(username, password)
    if user:
        return jsonify({"ok": True})
    return jsonify({"ok": False})


@app.route("/admin/ping")
def ping_route():
    host = request.args.get("host")
    return jsonify({"code": ping_host(host)})


@app.route("/admin/log")
def log_route():
    name = request.args.get("name")
    return read_log(name)


@app.route("/admin/calc")
def calc_route():
    expr = request.args.get("expr")
    return jsonify({"result": calculate(expr)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
