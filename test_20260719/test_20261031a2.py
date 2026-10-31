# SQL Serverに接続するプログラム
import mysql.connector

# コネクションの作成
conn = mysql.connector.connect(
    host='172.29.143.155',
    port=3306, ## PORT番号は整数値
    user='takashi',
    password='nanako',
    database='avtest01'
)

cursor = conn.cursor()
try:
    cursor.execute("SELECT * FROM avgal_list_001 ORDER BY id DESC;")
    rows = cursor.fetchall()
    ##print(rows)
    for row in rows:
        ##print(row[0],row[1],row[2])
        print(*row,sep=',')
finally:
    cursor.close()
    conn.close()