from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/redirect")
def ayo_redirect_about():
    return redirect(url_for("about"))

@app.route("/redirect")
def ayo_redirect__index():
    return redirect(url_for("index"))

@app.route("/redirect")
def ayo_redirect_contact():
    return redirect(url_for("contact"))

@app.route("/redirect")
def ayo_redirect_project():
    return redirect(url_for("project"))

if __name__ == "__main__":
    app.run(debug=True)