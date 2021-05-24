
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/mahalo/")
def mahalo_page():
	return render_template("mahalo.html")

@app.route("/crystal/")
def crystal_page():
	return render_template("crystal.html")

@app.route("/siren/")
def siren_page():
	return render_template("siren.html")

@app.route("/umpalumpa/")
def umpalumpa_page():
	return render_template("umpalumpa.html")

@app.route("/la_liberte/")
def la_liberte_page():
	return render_template("la_liberte.html")


if __name__=="__main__":
	debug=True
	host="0.0.0.0"
	app.run(host,debug=debug)

