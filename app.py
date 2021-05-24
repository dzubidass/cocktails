
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

cocktails=Flask(__name__)

@cocktails.route("/")
def index():
	return render_template("index.html")

@cocktails.route("/mahalo/")
def mahalo_page():
	return render_template("mahalo.html")

@cocktails.route("/crystal/")
def crystal_page():
	return render_template("crystal.html")

@cocktails.route("/siren/")
def siren_page():
	return render_template("siren.html")

@cocktails.route("/umpalumpa/")
def umpalumpa_page():
	return render_template("umpalumpa.html")

@cocktails.route("/la_liberte/")
def la_liberte_page():
	return render_template("la_liberte.html")


if __name__=="__main__":
	debug=True
	host="0.0.0.0"
	cocktails.run(host,debug=debug)

