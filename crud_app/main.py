import pymysql
from app import app
from tab import Results
from db_config import mysql
from flask import flash, render_template, request,redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/new_user')
def add_user_view():
    return render_template('add.html')

@app.route('/add',methods=['POST'])
def add_user():
    conn=None
    cursor=None
    try:
        _name=request.form['inputName']
        _email=request.form['inputEmail']
        _password=request.form['inputPassword']
        if _name and _email and _password and request.method == 'POST':
            _hashed_password=generate_password_hash(_password)
            sql="INSERT INTO tbl_user (user_name,user_email,user_password) VALUES (%s,%s,%s)"
            data = (_name,_email,_hashed_password)
            conn=mysql.connect() #from db_config file database instanace is mysql
            cursor=conn.cursor()
            print("conected")
            cursor.execute(sql,data)
            print("execution done")
            conn.commit()
            print("commit done")
            flash("User added Successfully!")
            return redirect(url_for('users'))
        else:
            return "<h1>ERROR WHILE ADDING USER</h1>"
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/')
def users ():
    conn=None
    cursor=None
    try:
        conn=mysql.connect()
        cursor=conn.cursor(pymysql.cursors.DictCursor) #just gets data as a dictionary
        cursor.execute("SELECT * FROM tbl_user")
        rows=cursor.fetchall()
        table=Results(rows)    
        table.border=True
        return render_template('users.html',table=table)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/edit/<int:id>')
def edit_view(id):
    conn=None
    cursor=None
    try:
        conn=mysql.connect()
        cursor=conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("SELECT * FROM tbl_user WHERE user_id= %s",id)
        row=cursor.fetchone()
        if row:
            return render_template('edit.html',row=row)
        else:
            return 'ERROR LOADING #{id}'.format(id=id)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update',methods=['POST'])
def update_user():
    conn=None
    cursor=None
    try:
        _name=request.form['inputName']
        _email=request.form['inputEmail']
        _password=request.form['inputPassword']
        _id=request.form['id']
        if _name and _email and _password and _id and request.method =="POST":
            _hashed_password=generate_password_hash(_password)
            print(_hashed_password)
            sql="UPDATE tbl_user SET user_name=%s, user_email=%s,user_password=%s WHERE user_id=%s"
            data=(_name,_email,_hashed_password,_id)
            conn=mysql.connect()
            cursor=conn.cursor()
            cursor.execute(sql,data)
            conn.commit()
            flash("USER UPDATED SUCCESSFULLY!")
            return redirect(url_for('users'))
        else:
            return 'Error while updating user'
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/delete/<int:id>')
def delete_user(id):
    conn=None
    cursor=None
    try:
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM tbl_user WHERE user_id=%s",(id,))
        conn.commit()
        flash("User deleted successfully!")
        return redirect(url_for('users'))
    except Exception as e:
        return(str(e))
    finally:
        cursor.close()
        conn.close()

if __name__=="__main__":
    app.run(debug=True)
