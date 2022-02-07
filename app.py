from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root123@localhost/db_mini"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "xxx"
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
   id = request.form.get('id')
   email = request.form.get('email')
   try:
    db.engine.execute(f"insert into user values ('{name}' ,'{country}', {id}, '{email}' ) ")
   except Exception as e:
    print(e)
    db.session.rollback()
    flash("Some error occured" , "danger" )
    return redirect(url_for('users'))
   flash('user added')
   return redirect(url_for('users'))

@app.route('/edit_user/<int:idx>'  , methods=['GET' , 'POST'])
def edit_user(idx):
    name = request.form.get('name')
    country = request.form.get('country')
    id = request.form.get('id')
    email = request.form.get('email')
    
    try:
        db.engine.execute(f'update user set name = {name} , country = {country}, ID = {id}, GMAIL = {email} where id = {idx} ')
    except Exception:
        db.session.rollback()
        flash("Some error occured" , "danger")
        return redirect(url_for('users'))
    flash('updated user')
    return redirect(url_for('users'))



@app.route('/delete_user/<int:idx>' , methods=['GET' , 'POST'])
def delete_user(idx):
    try:
        db.engine.execute(f'delete from user where id = {idx}')
    except Exception as e:
        print(e)
        db.session.rollback()
        flash("Some error occured" , "danger")
        return redirect(url_for('users'))
    flash('Deleted user')
    return redirect(url_for('users'))



@app.route("/blogs")
def blogs():
    blogs = db.engine.execute('select * from blogs')
    blogs_list = [row for row in blogs]
    return render_template('blogs.html', blogs_list = blogs_list)

@app.route('/add_blog' , methods=['GET' , 'POST'])
def add_blog():
   topic = request.form.get('topic')
   id = request.form.get('id')
   name = request.form.get('name')
   description = request.form.get('description')
   try:
    db.engine.execute(f"insert into blogs values ('{topic}' ,{id}, '{name}', '{description}' ) ")
   except Exception as e:
    print(e)
    db.session.rollback()
    flash("Some error occured" , "danger" )
    return redirect(url_for('blogs'))
   flash('blog added')
   return redirect(url_for('blogs'))

@app.route('/edit_user/<int:idx>'  , methods=['GET' , 'POST'])
def edit_blog(idx):
    topic = request.form.get('topic')
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    
    try:
        db.engine.execute(f'update user set topic = {topic} , id = {id}, name = {name}, description = {description} where id = {idx} ')
    except Exception:
        db.session.rollback()
        flash("Some error occured" , "danger")
        return redirect(url_for('blogs'))
    flash('updated blog')
    return redirect(url_for('blog'))



@app.route('/delete_blog/<int:idx>' , methods=['GET' , 'POST'])
def delete_blog(idx):
    try:
        db.engine.execute(f'delete from blogs where id = {idx}')
    except Exception as e:
        print(e)
        db.session.rollback()
        flash("Some error occured" , "danger")
        return redirect(url_for('blogs'))
    flash('Deleted blog')
    return redirect(url_for('blogs'))

  


@app.route("/contests")
def contests():
    return render_template('contests.html')

@app.route("/problems")
def problems():
    return render_template('problems.html')

if __name__ == "__main__":
    app.run(debug=True)