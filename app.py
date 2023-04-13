from flask import Flask, render_template, url_for

app= Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/sobrenos")
def sobrenos():
    return render_template("sobrenos.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

