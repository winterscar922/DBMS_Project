from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import *


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


@app.route('/users')
def users():
	users = db.engine.execute('select * from user')
	users_list = [row for row in users]
	return render_template('users.html' , users_list = users_list)

@app.route('/add_user' , methods=['GET' , 'POST'])
def add_user():
	name = request.form.get('name')
	country = request.form.get('country')
	try:
		db.engine.execute(f'insert into user values {name} ,{country} ')
	except Exception:
		db.session.rollback()
		flash("Some error occured" , "danger" )
        return redirect(url_for('users'))
	flash('user added')
	return redirect(url_for('users'))


@app.route('/edit_user/<int:idx>'  , methods=['GET' , 'POST'])
def edit_user(idx):
	name = request.form.get('name')
	country = request.form.get('country')
	try:
		db.engine.execute(f'update user set name = {name} , country = {country} where id = {idx} ')
	except Exception:
		db.session.rollback()
		flash("Some error occured" , "danger" )
        return redirect(url_for('users'))
	flash('updated user')
	return redirect(url_for('users'))


@app.route('/delete_user/<int:idx>' , methods=['GET' , 'POST'])
def delete_user(idx):
	try:
		db.engine.execute(f'delete from user where id = {idx}')
	except Exception:
		db.session.rollback()
		flash("Some error occured" , "danger" )
        return redirect(url_for('users'))

	flash('deleted user')
	return redirect(url_for('users'))


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
