import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="ap2506",database="resultapp")

mycursor = mydb.cursor()
mycursor.execute("select * from student_info")

for i in mycursor:
    print(i)
