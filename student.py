import pymysql

f = open(r"student_info.csv","r")
fstring = f.read()
#print(fstring)
flist = []
for line in fstring.split('\n'):
    flist.append(line.split(','))
#print(flist[1][0])

db = pymysql.connect("localhost","root","ap2506","resultapp")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT_INFO")

Name = flist[0][0]; Roll = flist[0][1]

queryCreateStudentTable = """CREATE TABLE STUDENT_INFO(
                            {} varchar(255) not null,
                            {} int
                            )""".format(Name, Roll)

cursor.execute(queryCreateStudentTable)



del flist[0]
#del flist[-1]
#print(len(flist))
#print(flist)

rows = ''
for i in range(len(flist)-1):
    rows += "('{}','{}')".format(flist[i][0],flist[i][1])
    if i!= len(flist)-2:
        rows+= ','

#print(rows)
queryInsert = "INSERT INTO STUDENT_INFO VALUES" + rows

try:
    cursor.execute(queryInsert)
    db.commit()

except:
    db.rollback()
db.close()
