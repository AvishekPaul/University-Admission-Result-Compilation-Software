import pymysql

f = open(r"codeRoll.csv","r")
fstring = f.read()
#print(fstring)
flist = []
for line in fstring.split('\n'):
    flist.append(line.split(','))
#print(flist[1][0])

db4 = pymysql.connect("localhost","root","ap2506","resultapp")

cursor = db4.cursor()

cursor.execute("DROP TABLE IF EXISTS Roll_Code")

Code = flist[0][0]; Roll = flist[0][1]

queryCreateRollCode = """CREATE TABLE Roll_Code(
                            {} varchar(255) not null,
                            {} int
                            )""".format(Code, Roll)

cursor.execute(queryCreateRollCode)



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
queryInsert = "INSERT INTO Roll_Code VALUES" + rows

try:
    cursor.execute(queryInsert)
    db4.commit()

except:
    db4.rollback()
db4.close()
