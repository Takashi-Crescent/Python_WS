# SQL Serverに接続するプログラム
import pyodbc
import pprint

def login():
    connect = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=192.168.1.101;"
    "DATABASE=IMFS;"
    "PORT=1433;"
    "UID=takashi;"
    "PWD=nanako")
    return connect

##connect= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';PORT=1433;Trusted_Connection='+trusted_connection+';')
conn = login()
cursor = conn.cursor()
cursor.execute("SELECT TOP(1000) * FROM [IMFS].[dbo].[T0101_0017_売上明細] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00'")
rows = cursor.fetchall()
pprint.pprint(rows)
print(pyodbc.drivers())

i = 0
for r in rows:
    if i > 100:
        break
    print(r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19]) 
    i = i + 1

cursor.close()
conn.close()
