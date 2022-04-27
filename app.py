from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    words = ["Pluslasku", "Miinuslasku", "Kertolasku", "Jakolasku", "Laskujärjestys", "Prosenttilasku", "Kertoma"]
    return render_template("index.html", message="Opetuspakat:", items=words)

@app.route("/login")
def login():
    return render_template("login.html", message="Kirjaudu sisään")

@app.route("/registration")
def registration():
    return render_template("registration.html", message="Luo uusi tunnus")

@app.route("/plus")
def plus():
    return render_template("plus.html", message="Kirjoita vastaus ruutuun:")

@app.route("/miinus")
def miinus():
    return render_template("miinus.html", message="Kirjoita vastaus ruutuun:")

@app.route("/kerto")
def kerto():
    return render_template("kerto.html", message="Kirjoita vastaus ruutuun:")

@app.route("/jako")
def jako():
    return render_template("jako.html", message="Kirjoita vastaus ruutuun:")

@app.route("/prosentti")
def prosentti():
    return render_template("prosentti.html", message="Kirjoita vastaus ruutuun:")

@app.route("/kertoma")
def kertoma():
    return render_template("kertoma.html", message="Kirjoita vastaus ruutuun:")