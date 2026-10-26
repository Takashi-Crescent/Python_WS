# SQL Serverに接続するプログラム
import pyodbc
import pprint
import pandas as pd

"""
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=192.168.1.102;"
    "DATABASE=IMFS;"
    "PORT=1433;"
    "UID=takashi;"
    "PWD=nanako"
)

##connect= pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';PORT=1433;Trusted_Connection='+trusted_connection+';')

cursor = conn.cursor()
cursor.execute("SELECT TOP(1000) * FROM [IMFS].[dbo].[T0101_0017_売上明細] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00'")
rows = cursor.fetchall()
pprint.pprint(rows)

cursor.close()
conn.close()
"""

## SQL Serverに接続する関数
def login():
    connect = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=192.168.1.102;"
        "DATABASE=IMFS;"
        "PORT=1433;"
        "UID=takashi;"
        "PWD=nanako"
    )
    return connect

## SQL Serverに接続する関数を呼び出してクエリを発行する。
print(pyodbc.drivers())
conn = login()
cursor = conn.cursor()
## cursor.execute("SELECT TOP(1000) * FROM [IMFS].[dbo].[T0101_0017_売上明細] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00'")
## cursor.execute("SELECT [行番号] FROM [IMFS].[dbo].[T0101_0017_売上明細_TEST] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00' ORDER BY [行番号] DESC")
#cursor.execute("SELECT * FROM [IMFS].[dbo].[T0101_0017_売上明細_TEST] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00' ORDER BY [行番号] DESC")
#rows = cursor.fetchall()
#pprint.pprint(rows)

#cursor.close()
#conn.close()

query = "SELECT * FROM [IMFS].[dbo].[T0101_0017_売上明細_TEST] where [日付・時刻] >= '2018-03-01 00:00:00' and [日付・時刻] < '2018-03-02 00:00:00'"
df = pd.read_sql(query, conn)
print(df)
print("CSVファイルに出力します。")
df.to_csv('test_20260719/output.csv', index=False, encoding='utf-8-sig')  # CSVファイルに出力

cursor.close()
conn.close()
