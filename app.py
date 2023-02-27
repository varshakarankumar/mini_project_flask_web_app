from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy as sq
app = Flask(__name__)

@app.route("/submit")
def submit():
    return render_template('index.html')

@app.route("/")
def hello():
    return render_template('toincss.html')

@app.route("/pro")
def products():
    return "<p>products</p>"

if __name__=="__main__":
    app.run(debug=True)