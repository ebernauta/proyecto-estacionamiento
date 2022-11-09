from flask import Flask, jsonify, render_template, redirect, url_for, request, flash
from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/main', methods=["POST", "GET"])
def main():
    
    if request.method == "POST":
        dato = request.form['dato']
        return f"El dato es: {dato}"
    
    return render_template("scan.html")


if __name__ == '__main__':    
    app.run(debug=True)