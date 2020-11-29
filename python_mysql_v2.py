import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from datetime import datetime
# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root"
# )
# mycursor=db.cursor()
# mycursor.execute("CREATE DATABASE testdatabase")
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor=db.cursor()

#table created
#mycursor.execute("CREATE TABLE Person (name VARCHAR(50),age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)") 
#SMALLINT -32K TO 32K AND UNSIGNED, personID is uniqe id, Autoincrement will allow diffrent keys 

#----------------------------------------------------------#
#describe table

# mycursor.execute("DESCRIBE Person") #description of table
# for i in mycursor:
#     print(i)

#----------------------------------------------------------#
#entry created

# sql_formula_insert="insert into Person(name,age) values(%s,%s)"
# entry=("Tareeb",20)
# mycursor.execute(sql_formula_insert,entry)
# db.commit()

# sql_formula_view="select * from Person"
# mycursor.execute(sql_formula_view)
# for i in mycursor:
#     print(i)
#----------------------------------------------------------#
#NEW TABLE
#mycursor.execute("CREATE TABLE Test (id int primary key not null auto_increment,name varchar(50) not null, created_on datetime not null, gender ENUM('M','F','O') NOT NULL)")
#ENUM is a string object whose value is fixed in a list

# SQL_FORMULA_INSERT="insert into Test(name, created_on, gender) values(%s,%s,%s)"
# entry=("Ahmed",datetime.now(),"M")
# mycursor.execute(SQL_FORMULA_INSERT,entry)
# db.commit()
# sql_formula_view="select * from Test"
# mycursor.execute(sql_formula_view)
# for i in mycursor:
#     print(i)

#delete segment
# sql_formula_delete="DELETE FROM Test where id=5"
# mycursor.execute(sql_formula_delete)
# db.commit()
# sql_formula_view="select * from Test where gender = 'M' order by id DESC"
# mycursor.execute(sql_formula_view)
# for i in mycursor:
#     print(i)

#---------------------------------------------------------------------------#
#ALTER TABLE
#mycursor.execute("ALTER TABLE Test ADD column Food varchar(50) NOT NULL")
#mycursor.execute("ALTER TABLE Test DROP column Food") #DROP COLUMN
#mycursor.execute("ALTER TABLE Test CHANGE name complete_name varchar(10)") #change column name but requires type as well but shouldnt be less than initial value


