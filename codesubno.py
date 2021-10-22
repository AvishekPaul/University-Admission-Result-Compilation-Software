import pymysql

f = open(r"codeSubNo.csv","r")
fstring = f.read()
#print(fstring)
flist = []
for line in fstring.split('\n'):
    flist.append(line.split(','))
#print(flist[1][0])

db2 = pymysql.connect("localhost","root","ap2506","resultapp")

cursor = db2.cursor()

cursor.execute("DROP TABLE IF EXISTS Code_SubNumber")

Code = flist[0][0]; Physics = flist[0][1]; Math = flist[0][2]; Chemistry = flist[0][3]; English = flist[0][4]


queryCreateCodeAndNumber = """CREATE TABLE Code_SubNumber(
                            {} varchar(255) not null,
                            {} int,
                            {} int,
                            {} int,
                            {} int
                            )""".format(Code,Physics,Math,Chemistry,English)


cursor.execute(queryCreateCodeAndNumber)



del flist[0]
#del flist[-1]
#print(len(flist))
#print(flist)

rows = ''
for i in range(len(flist)-1):
    rows += "('{}','{}','{}','{}','{}')".format(flist[i][0],flist[i][1],flist[i][2],flist[i][3],flist[i][4])

    if i!= len(flist)-2:
        rows+= ','

#print(rows)
queryInsert = "INSERT INTO Code_SubNumber VALUES" + rows

try:
    cursor.execute(queryInsert)
    db2.commit()

except:
    db2.rollback()
db2.close()
