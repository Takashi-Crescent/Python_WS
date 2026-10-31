# SQL Serverに接続するプログラム
import pymysql
import random

# コネクションの作成
conn = pymysql.connect(
    host='172.29.143.155',
    port=3306, ## PORT番号は整数値
    user='takashi',
    password='nanako',
    database='avtest01'
)

try:
    with conn.cursor() as cursor:
        ##cursor=conn.cursor()
        cursor.execute("SELECT * FROM avgal_list_001 ORDER BY id ASC;")
        rows = cursor.fetchall()
        ##print(rows)
        
        #i = 0
        #for row in rows:
           #print(row)
           #print(*row,sep=',')
           #array = list(row)
           #array.append(i)
           #print(array)
           #i += 1
        print(rows)
        #print(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5])
        #print(len(rows))
        #for i in range(1000):
        #    print(rows[random.randint(0, len(rows)-1)])
        print("=======================================")
        i = random.randint(0, len(rows)-1)
        print(rows[i])
        print(rows[i][1],rows[i][2])
        #print("i=",i)
        print("=======================================")
        
        for i in range(0,len(rows),1):
            print(rows[i][1],rows[i][2])

except Exception as e:  #### Tryブロック内で例外発生した場合の処理ブロック ####
    print("Error:", e)
else: #### Tryブロック内の全ての処理で例外が発生しなかった場合の処理ブロック ####    
    print("\n")
    i=0
    while (i < len(rows)):
        print(rows[i][1],rows[i][2])
        i += 1

    print("すべての処理に成功しました。")
finally: #### Tryブロック内の例外発生の有無にかかわらずに必ず実行される処理ブロック ####
    conn.close()
