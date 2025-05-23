from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("about.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/projects/instrumenty")
def project_details():
    return render_template("instrumenty.html")

@app.route("/projects/instrumenty/aplikacjaInstrumenty")
def project1():
    return render_template("aplikacjaInstrumenty.html")

if __name__ == "__main__":
    app.run(debug=True)