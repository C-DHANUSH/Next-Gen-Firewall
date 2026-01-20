from flask import Flask, render_template, request, redirect, session

# Internal modules
from auth import login_user, register_user
from analytics import firewall_stats
from firewall_rules import add_rule, get_rules, toggle_rule, get_logs
from ip_filter import block_ip

app = Flask(__name__)
app.secret_key = "nextgen_firewall_secret_key"


# ================= AUTH =================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = login_user(request.form)
        if user:
            session["user"] = request.form["username"]
            return redirect("/dashboard")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register_user(request.form)
        return redirect("/")
    return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ================= DASHBOARD =================

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    stats = firewall_stats()
    return render_template("dashboard.html", stats=stats)


# ================= FIREWALL =================

@app.route("/firewall", methods=["GET", "POST"])
def firewall():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        website = request.form["website"]
        action = request.form["action"]
        add_rule(website, action)
        return redirect("/firewall")

    rules = get_rules()
    logs = get_logs()
    return render_template("firewall.html", rules=rules, logs=logs)


@app.route("/toggle/<int:id>")
def toggle(id):
    if "user" not in session:
        return redirect("/")
    toggle_rule(id)
    return redirect("/firewall")


@app.route("/logs")
def logs():
    if "user" not in session:
        return redirect("/")
    return render_template("logs.html", logs=get_logs())


# ================= IP BLOCK =================

@app.route("/block-ip", methods=["POST"])
def blockip():
    if "user" not in session:
        return redirect("/")
    block_ip(request.form["ip"], request.form["reason"])
    return redirect("/dashboard")


# ================= MAIN =================

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/logs-data")
def logs_data():
    return "<br>".join(get_logs()[-20:])
