# SQL Serverに接続するプログラム
import pyodbc
import pprint


def login():
    "DRIVER={SQL Server};"
    "SERVER=192.168.1.102;"
    "DATABASE=IMFS;"
    "PORT=1433;"
    "UID=takashi;"
"PWD=nanako"


##connect= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';PORT=1433;Trusted_Connection='+trusted_connection+';')

cursor = conn.cursor()
cursor.execute("SELECT TOP(1000) * FROM [IMFS].[dbo].[T0101_0017_売上明細] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00'")
rows = cursor.fetchall()
pprint.pprint(rows)

cursor.close()
conn.close()


