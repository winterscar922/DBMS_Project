from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root123@localhost/dbms_mini"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    users = db.engine.execute('Select * from user')
    users_list = [ row for row in users]
    print(users_list)
    return render_template('index.html',  users_list=users_list)

@app.route("/users")
def users():
    return render_template('users.html')

@app.route("/blogs")
def blogs():
    return render_template('blogs.html')

@app.route("/contests")
def contests():
    return render_template('contests.html')

@app.route("/problems")
def problems():
    return render_template('problems.html')

if __name__ == "__main__":
    app.run(debug=True)