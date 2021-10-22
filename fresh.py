import pymysql
import csv

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


#part 2
# Number of the subjects against roll
#...............................................

f2 = open(r"codeSubNo.csv","r")
fstring2 = f2.read()
#print(fstring)
flist2 = []
for line2 in fstring2.split('\n'):
    flist2.append(line2.split(','))
#print(flist[1][0])

db2 = pymysql.connect("localhost","root","ap2506","resultapp")

cursor = db2.cursor()

cursor.execute("DROP TABLE IF EXISTS Code_SubNumber")

Code = flist2[0][0]; Physics = flist2[0][1]; Math = flist2[0][2]; Chemistry = flist2[0][3]; English = flist2[0][4]


queryCreateCodeAndNumber = """CREATE TABLE Code_SubNumber(
                            {} varchar(255) not null,
                            {} int,
                            {} int,
                            {} int,
                            {} int
                            )""".format(Code,Physics,Math,Chemistry,English)


cursor.execute(queryCreateCodeAndNumber)



del flist2[0]
#del flist[-1]
#print(len(flist))
#print(flist)

rows2 = ''
for i in range(len(flist2)-1):
    rows2 += "('{}','{}','{}','{}','{}')".format(flist2[i][0],flist2[i][1],flist2[i][2],flist2[i][3],flist2[i][4])

    if i!= len(flist2)-2:
        rows2+= ','

#print(rows)
queryInsert = "INSERT INTO Code_SubNumber VALUES" + rows2

try:
    cursor.execute(queryInsert)
    db2.commit()

except:
    db2.rollback()
db2.close()

#part 3
#..........................
# Code against roll
#roll_code..............

f3 = open(r"codeRoll.csv","r")
fstring3 = f3.read()
#print(fstring)
flist3 = []
for line3 in fstring3.split('\n'):
    flist3.append(line3.split(','))
#print(flist[1][0])

db4 = pymysql.connect("localhost","root","ap2506","resultapp")

cursor = db4.cursor()

cursor.execute("DROP TABLE IF EXISTS Roll_Code")

Code = flist3[0][0]; Roll = flist3[0][1]

queryCreateRollCode = """CREATE TABLE Roll_Code(
                            {} varchar(255) not null,
                            {} int
                            )""".format(Code, Roll)

cursor.execute(queryCreateRollCode)



del flist3[0]
#del flist[-1]
#print(len(flist))
#print(flist)

rows3 = ''
for i in range(len(flist3)-1):
    rows3 += "('{}','{}')".format(flist3[i][0],flist3[i][1])
    if i!= len(flist3)-2:
        rows3+= ','

#print(rows)
queryInsert = "INSERT INTO Roll_Code VALUES" + rows3

try:
    cursor.execute(queryInsert)
    db4.commit()

except:
    db4.rollback()
db4.close()


#result compilation
#part-4............................

db5 = pymysql.connect("localhost","root","ap2506","resultapp")

cursor = db5.cursor()
cursor.execute("DROP TABLE IF EXISTS Result")

cursor.execute("CREATE TABLE Result (Code varchar(255) not null,Roll int, TotalNumber int)")



#cursor.execute(queryCreateResultTable)

query = "INSERT INTO Result SELECT Code_SubNumber.Code, STUDENT_INFO.Roll, (Physics+Math+Chemistry+English) AS TotalNumber From STUDENT_INFO,Code_SubNumber,ROLL_CODE WHERE STUDENT_INFO.Roll=ROLL_CODE.Roll AND Code_SubNumber.Code=ROLL_CODE.Code ORDER BY TotalNumber DESC,Physics DESC,Math DESC,Chemistry DESC,English DESC"
cursor.execute(query)
query2 = "SELECT * from Result"

try:

    cursor.execute(query2)
    result=cursor.fetchall()
    #print(result)
    position = 0
    #print("Code\tROll\tTotalNumber\tPosition\n-----------------------------------")
    res = []
    finalres = [["Code","Roll","TotalNumber","Position"]]
    for i in result:

        code = i[0]
        res.append(code)
        roll = i[1]
        res.append(roll)
        TotalNumber = i[2]
        res.append(TotalNumber)
        position=position+1
        res.append(position)

    i=0
    while i<len(res):
        finalres.append(res[i:i+4])
        i=i+4

    with open('result5.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(finalres)

    csvFile.close()
    #print(resul)




    #cursor.execute()
    db5.commit()

except:
    db5.rollback()
    print("unable")
db5.close()
