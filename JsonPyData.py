import psycopg2.extras
import json
import sys
conn = psycopg2.connect(database="Test_demo", user = "sabbir_05", password = "one2one", host = "127.0.0.1", port = "5432")

# if conn:
#     print("Successfully Connected")
# else:
#     print("Not Connected")

j = json.load(open('d:/VSCODE/DataConnect/data.json'))

car = conn.cursor()
car.execute('''CREATE TABLE IF NOT EXISTS JsonData
      (uuid varchar PRIMARY KEY     NOT NULL,
      date           varchar    NOT NULL,
      min            NUMERIC     NOT NULL,
      max        NUMERIC,
      Avg         Numeric);''')
#print ("Table created successfully")




#------------- Data Insert-------------

for x in range(len(j)):
    uuid = j[x]['uuid']
    date = j[x]['data']
    min = j[x]['min']
    max = j[x]['max']
    Avg = j[x]['avg']
    InsertData = (uuid,date,min,max,Avg)
    car.execute("INSERT INTO JsonData (uuid,date,min,max,Avg) VALUES(%s,%s,%s,%s,%s)",InsertData)

conn.commit()
car.close()

#--------Update Value---

