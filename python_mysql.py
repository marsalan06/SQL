import mysql.connector
#-----------------------------------------------------#
#before creating data base
# mydb=mysql.connector.connect(
#     host="localhost",
#     user="root", 
#     passwd="root"
# ) 

#----------------------------------------------------#
#after creating db
mydb=mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="root",
    database="testdb"
)
#user and passwd == root, in server config

print(mydb) #prints object memory location

mycursor=mydb.cursor() #cursor object instiated on db



#------------------------------------------------------#
#database created, see in workbench under schema
#mycursor.execute("CREATE DATABASE testdb") 

#sql command to show db
# mycursor.execute("SHOW DATABASES")
# for db in mycursor: 
#     print(db) #shows all data bases in tuple

#------------------------------------------------------#
#create table in db
#CREATE TABLE name_of_table (name_of_column or feild TYPE(range of characters accepted), name_of_column or feild TYPE(range of characters accepted) )
#mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))") #created, shown in workbench

#to view tables in db
# mycursor.execute("SHOW TABLES")
# for t in mycursor:
#     print(t)

#-------------------------------------------------------#
#to insert data in the table 
#create a genralize comand in a variable to create reusability and use %s as place holder

#sql_formula="INSERT INTO students(name,age) VALUES (%s, %s)"
#student1=("LAIBA",23) #entry created as tuple 

#mycursor.execute(sql_formula,student1)#executing genral command with values 
#mydb.commit() #like git commit , execute is track while commit creates breakpoint and pushes

#to view in work bench ... USE testdb --> select * from students --> shows all rows and columns

# student1=[("Javeria",24),("saba",25),("sabiha",25),("sajahar",24),("khadija",25)]
# mycursor.executemany(sql_formula,student1)
# mydb.commit()
#------------------------------------------------------#
#to view data 

# sql_formula ="SELECT * FROM students where age=24" #query command of SQL 
# mycursor.execute(sql_formula)
# myresult=mycursor.fetchall() #fetchone() to get only one value
# for r in myresult:
#     print(r) #tuples returned

#-------------------------------------------------------#
# sql_formula ="SELECT * FROM students WHERE name LIKE '%a%' " 

#place holders % with LIKE keword
# #%dij% , shows entry that may contain dij i.e khadija 

# mycursor.execute(sql_formula)
#------------------------------------------------------#
# sql_formula="SELECT * FROM students WHERE name = %s "
# mycursor.execute(sql_formula,("saba",))
# my_result=mycursor.fetchall()
# for r in my_result:
#     print(r)
#------------------------------------------------------#
#to update value
# sql_formula= "UPDATE students SET age=13 WHERE name = 'sajahar'"
# mycursor.execute(sql_formula)
# mydb.commit()
# sql_formula="SELECT * from students limit 5 offset 4" # limits to 5 result after 4th 
# mycursor.execute(sql_formula)
# myresult=mycursor.fetchall()
# for i in myresult:
#     print(i)

#------------------------------------------------------#
#sorting technique

#sql_formula="SELECT * FROM students order by name"
#sql_formula="SELECT * FROM students order by age DESC"
# sql_formula="SELECT * FROM students order by age ASC"
# mycursor.execute(sql_formula)
# myresult=mycursor.fetchall()
# for i in myresult:
#     print(i)
#------------------------------------------------------#
# sql_formula = "insert into students (name,age) values (%s,%s)"
# student=("sajahar",13)
# mycursor.execute(sql_formula,student)
# mydb.commit()
# sql_formula="select * from students"
# mycursor.execute(sql_formula)
# myresult=mycursor.fetchall()
# for i in myresult:
#     print(i)

# #to delete entry 
# sql_formula="delete from students where name='sajahar'"
# mycursor.execute(sql_formula)
# mydb.commit()
# sql_formula="select * from students"
# mycursor.execute(sql_formula)
# my_result=mycursor.fetchall()
# for i in my_result:
#     print(i)
    
#--------------------------------------------------------#
#delete table 
# sql_formula="DROP TABLE IF EXIST students"
# mycursor.execute(sql_formula)
# mydb.commit()
#--------------------------------------------------------#
