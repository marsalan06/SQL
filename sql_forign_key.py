import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from datetime import datetime

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)
mycursor=db.cursor()

#create table 1
Q1="create TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50) ) "
Q2="create TABLE Scores (userID int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
#mycursor.execute(Q1)
#mycursor.execute(Q2)

Q3="Describe Scores"
# mycursor.execute(Q3)
# for i in mycursor:
#     print (i)

Q4="Show TABLES"
# mycursor.execute(Q4)
# for i in mycursor:
#     print(i)

Users_list=[("Arsalan","ArsalanSQL"),("Kashaf","Ketchup"),("Ahmed","ahmed_tep")]
Scores_list=[(30,45),(55,23),(56,63)]
# mycursor.executemany("INSERT INTO Users (name, passwd) VALUES(%s,%s)",Users_list)
Q5="INSERT INTO Users (name, passwd) VALUES(%s,%s)"
#or use this technique
Q6="INSERT INTO Scores(userID,game1,game2) VALUES(%s,%s,%s)"
# for x,user in enumerate(Users_list):
#     mycursor.execute(Q5,user)
#     last_id=mycursor.lastrowid #on each iteration gets the id value from column
#     mycursor.execute(Q6,(last_id,)+Scores_list[x]) #tuple additon to join scores with id

# db.commit()
mycursor.execute("select * from Scores")
for x in mycursor:
    print(x)