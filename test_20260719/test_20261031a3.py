# SQL Serverに接続するプログラム
import pymysql

# コネクションの作成
conn = pymysql.connect(
    host='172.29.143.155',
    port=3306, ## PORT番号は整数値
    user='takashi',
    password='nanako',
    database='avtest01'
)

cursor=conn.cursor()
cursor.execute("SELECT * FROM avgal_list_001 ORDER BY id ASC;")
rows = cursor.fetchall()
conn.close()

# タプルを表示する。
print("####  タプルを表示  ####")
print(rows) ## タプルを表示する。
print()

# タプルのリストを反復処理
print("#### タプルのリストを反復処理  ####")
for row in rows:
    for item in row:
        print(item,end='\t') ## 文字の最後にはタブコードを挿入
    print()

# タプルのリストをアンパック
print("#### タプルのリストをアンパック  ####")
for a,b,c in rows:
    print(f"""a={a},b={b},c={c}""")

# タプルのリストをソート
# lambda x:x[2]と記述することで、各タプルの3番目の要素（インデックス3）を基準にソートされます。
print("####  タプルのリストをソート  ####")
sorted_rows = sorted(rows, key=lambda x:x[2] )
print(sorted_rows)

# タプルのリストを検索
# リスト内包表記を使って、タプルのリストrowsから特定の値search_keyを持つ要素を検索しています。
#[item for row in matrix for item in row if item == search_key] という記述は、次の手順で処理されます。

#rowsの各行rowに対して、rowの各要素itemがsearch_keyと等しいかをチェックし、等しい場合、そのitemをリストに追加する。
#実行結果から、search_keyである27が2つ見つかり、リスト[27,27]が出力されていることがわかります。
#リスト内包表記を使うことで、ネストされたループと条件チェックを簡潔に記述できます。
print("#### タプルのリストを検索 ####")
#search_key='ジュリア'
search_key=27
found_items = [item for row in rows for item in row if item == search_key]
print (found_items)

# タプルのリストに新しい要素を追加する。
# タプルはイミュータブルであるので、要素は追加できない。
# タプルそのものは変更できないが、タプルを要素に持つリストであれば、新しいタプルを追加することができる。

print("#### タプルを要素に持つリストに要素を追加 ####")
new_row = (7,'二宮和香',36)
## rows.append(new_row) このコードはエラーになる。タプルはイミュータブルであるため。
rows2 = list(rows) ## タプルを要素に持つリストであれば、要素を追加できる。
rows2.append(new_row)
print(rows2)


# タプルのリストから要素を削除する。
# タプルはイミュータブルであるので、要素は削除できない。
# タプルそのものは削除できないが、タプルを要素に持つリストであれば、存在するタプルを削除することができる。
print("#### タプルを要素に持つリストに要素を削除 ####")
rows2.remove((5, 'AIKA', 36))
print(rows2)

# タプルのリストを変換する。
# タプルのリストをリストのリストに変換したり、その逆の変換をしたりする必要があります。

# (1)タプルのリストをリストのリストに変換
print("#### タプルのリストをリストのリストに変換 ####")
list_matrix = [list(row) for row in rows]
print(list_matrix)
# (2)リストのリストをタプルのリストに変換
print("#### リストのリストをタプルに変換 ####")
tuple_matrix = [tuple(row) for row in list_matrix]
print(tuple_matrix)