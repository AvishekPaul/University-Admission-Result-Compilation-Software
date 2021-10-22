import pymysql
import csv

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
