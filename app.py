from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root123@server/dbms_mini"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/users")
def users():
    return render_template('users.html')

if __name__ == "__main__":
    app.run(debug=True)