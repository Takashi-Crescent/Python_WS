### 乱数値を作成するテストプログラム
### 作成日: 2026-07-20 18:35
### 作成者: Takashi Masuda
### バージョン: 1.00

import os
import string
import random

##関数: 指定桁数の16進数の乱数値を作成する
### パラメータ: 作成したい乱数の桁数を指定する
### 戻り値: 16進数の乱数値
# 16進数(0-9,a-f)

# 定数の確認 0-9の数字であることを確認する。
print("定数の確認:",string.digits)

# ランダムに16桁のN進数を抽出する。
print("\nNo.1 ######################ランダムに16桁のN進数を抽出する。 Start ######################")
random_decimal = ''.join(random.choice(string.digits) for _ in range(16))
print("乱数値10進数: ",random_decimal)
# ランダムな16桁の16進数を抽出する。
random_hex = ''.join(random.choice(string.hexdigits) for _ in range(16))
print("乱数値16進数(小文字): ",random_hex.lower()) # 大文字で出力する。
print("乱数値16進数(大文字): ",random_hex.upper()) # 小文字で出力する。
# ランダムに16桁の8進数を抽出する。
random_octal = ''.join(random.choice(string.octdigits) for _ in range(16))
print("乱数値8進数: ",random_octal)
random_octal = ''.join(random.choice(string.octdigits) for _ in range(0,16,1))
print("乱数値8進数: ",random_octal)
print("No.1 ######################ランダムに16桁のN進数を抽出する。 End ######################")

#### ランダムな文字列(英字＋数字)を作成する関数を定義する。
def random_string(length=16):
    letters = string.ascii_lowercase + string.digits
    array = []

    for _ in range(length):
        value = random.choice(letters)
        array.append(value)

    return ''.join(array)

#### ランダムな文字列(英字＋数字)を作成する関数を定義する。
def random_alphabet_number(length=16): ## 引数のlengthのデフォルト値は16桁とする。
    ## アルファベット小文字a-zの26文字、数字0-9の10文字を連結した文字列を作成する。
    letters = string.ascii_lowercase + string.digits 
    ## 空の配列を定義する。ここに乱数値も文字を順次格納していく。
    yy = ""
    for i in range(0,length,1):
        x = random.choice(letters) ## lettersの中からランダムに1文字を抽出する。
        yy = yy + x.lower()
    return yy

#### ランダムな16進数を作成する関数を定義する。
def random_hex(length=16): ## 引数のlengthのデフォルト値は16桁とする。
    ## 16進数のランダム値を作成する。
    y3 = ""
    for i in range(0,length,1):
        x = random.choice(string.hexdigits)
        y3 = y3 + x.lower()
    return y3

def random_hex2(length=16):
    letters = string.hexdigits
    ## 空の配列を定義する。ここに乱数値も文字を順次格納していく。
    array = []
    ## 繰り返し処理で、指定桁数の乱数値を作成する。
    for _ in range(0,length,1):  ## 繰り返し変数を利用しない場合は、慣習的にアンダースコア(_)を使用する。
        value = random.choice(letters) ## lettersの中からランダムに1文字を抽出する。
        array.append(value.lower())  ## 抽出した乱数値を1文字づつ配列にセットする。
    return ''.join(array) ## 配列に格納された文字列を結合して、1つの文字列として返す。

print("\nNo.2 ###################### random_string() 関数利用のテストです。  Start ######################")
a = random_string() ## デフォルト値の16桁の乱数値を作成する。
b = random_string(length=32) ## 引数に32桁の乱数値を作成する。
print("a = " + a)  # ex. rrgz3j1u5vio54l3
print("b = " + b)  # ex. 6dxb04
print("No.2 ###################### random_string() 関数利用のテストです。  End ######################")

print("\nNo.3 ###################### 乱数値のテスト01です。 Start ######################")
print("16進数の乱数値を作成する。")
y1=""
for i in range(16):
    print("i=",i,", string=",random_string(length=16))
    x = random.choice(string.hexdigits)
    print("i=",i,", char=",x)
    y1 = y1 + x.lower()
str = [random.choice(string.hexdigits) for j in range(16)] ## 16桁の16進数の乱数値を作成する。

print("y1 = ",y1)
print("str= ",str) ## 配列に格納した16要素の16進数の乱数値を作成する。
print("str= ",''.join(str).lower())  ## 配列に格納した16要素の16進数の乱数値を結合して1つの文字列として出力する。
print("No.3 ###################### 乱数値のテスト01です。 End ######################")

print("\nNo.4 ###################### 乱数値のテスト02です。 Start######################")
y2=""
for i in range(0,16,1):   ## range(0,16,1)は、0から15までの整数を生成する。range(0,16)でも同じ結果になる。
    if (str[i].isdigit() == True): ## 数字である場合は、そのまま文字列として結合する。
        y2 = y2 + str[i]
    else: ## 数字でない場合(a,b,c,d,e,fの文字の場合)は、小文字に変換して結合する。
        y2 = y2 + str[i].lower()
print("16桁の16進数の乱数値02 = ",y2)
print("No.4 ###################### 乱数値のテスト02です。 End ######################")

### random_digits = ''.join(random.choice(string.digits) for _ in range(16))
print("\nNo.5 ###################### 乱数値のテスト03です。 Start ######################")
y3 = ""
for i in range(16): ## range(16)は、0から15までの整数を生成する。range(0,16)でも、range(0,16,1)でも同じ結果になる。
    x = random.choice(string.hexdigits) ## 16進数の文字列からランダムに1文字を抽出する。
    y3 = y3 + x.lower() ## 抽出した文字列を小文字に変換して結合する。
print("16桁の16進数の乱数値03 = ",y3)
print("No.5 ###################### 乱数値のテスト03です。 End ######################")

print("\nNo.6 ###################### 乱数値のテスト04です。 Start ######################")
y4 = ''.join(random.choice(string.hexdigits) for _ in range(16))
print("y4 = ",y4.lower())
print("No.6 ###################### 乱数値のテスト04です。 End ######################")

## 配列文字列の結合
print("\nNo.7 ###################### 乱数値(10進数)列の確認です。 Start ######################")
random_digits = ''.join(random.choice(string.digits) for _ in range(16))
print("16桁の10進数の乱数値 ",''.join(str).lower())
print("No.7 ###################### 乱数値(10進数)列の確認です。 End ######################")

## 16進数の乱数値
print("\nNo.8 ###################### 関数利用の確認です。 Start ######################")
print("random_hex01=",random_hex())
print("random_hex02=",random_hex(length=16))
print("random_hex03=",random_hex(length=32))
print("random_hex04=",random_hex2())
print("random_hex05=",random_hex2(length=16))
print("random_hex06=",random_hex2(length=32))
print("random_alphabet_number01=",random_alphabet_number())
print("random_alphabet_number02=",random_alphabet_number(length=16))
print("random_alphabet_number03=",random_alphabet_number(length=32))
print("No.8 ###################### 関数利用の確認です。 End ######################")

print("\nNo.9 ###################### random.choice()の確認です。 Start ######################")
fruits = ["りんご", "バナナ", "みかん"]
alphabet ="abcdefghijklmnopqrstuvwxyz"
chosen01 = random.choice(fruits)
chosen02 = random.choice(alphabet)

print("配列のランダム選択関数: 選択されたのは、"+chosen01+"です。")
print("文字列のランダム選択関数: 選択されたのは、"+chosen02+"です。")

hexnum = "0123456789abcdef"
chosen04 = ""
for _ in range(0,16,1):
    chosen03 = random.choice(hexnum)
    chosen04 = chosen04 + chosen03
print("選択された16進数は、"+chosen04+"です。") ## 
print("No.9 ###################### random.choice()の確認です。 End ######################")


## 辞書型のデータの確認
print("\nNo.10 ######################  辞書型データの確認01です。 Start ######################")
D={1:"a",2:"c",3:"d",4:"b"}
for n,a in D.items():
  print(n,a)

print("\nD.items()=",D.items(),"\n")

for ii,zz in D.items():
  print(ii,zz)
print("No.10 ######################  辞書型データの確認01です。 End ######################")


print("\nNo.11 ###################### 辞書型データの確認02です。 Start ######################")
XX={1:"Mio", 2:"Julia", 3:"Kyoko", 4:"Sora", 5:"Yuna", 6:"Reiko", 7:"Asami", 8:"Sumire01", 9:"Sumire02", 10:"Karen"}
for ii,yy in XX.items():
  print(ii,yy)
print("\n")

print(XX.keys())
print(XX.values())
print(XX.items())

i = 1
while i <= 10:
    print(i,XX[i])
    i = i + 1
XX[i] = "冬月かえで"
print("\n")
while i > 0:
    print(i,XX[i])
    i = i - 1
print("No.11 ######################  辞書型データの確認02です。 End ######################")

print("\nNo.12 ######################  辞書型データの確認03です。 Start ######################")
print("#### ------------------------------------------------ ####")
YY={"a":"Mio", "b":"Julia", "c":"Kyoko", "d":"Sora", "e":"Yuna", "f":"Reiko", "g":"Asami", "h":"Sumire01", "i":"Sumire02", "j":"Karen"}
i = 0
while i < 10:
#    print(XX.keys())
#    print(XX.values())
#    print(XX.items())
    print(i+1,list(YY.keys())[i],YY[list(YY.keys())[i]])
    i = i + 1
print("#### ------------------------------------------------ ####")
YY["k"] = "Kaede"
while i >= 0:
    print(i+1,list(YY.keys())[i],YY[list(YY.keys())[i]])
    i = i - 1

print(list(YY.keys()))
print(list(YY.keys())[0])
print(list(YY.values()))
print(list(YY.values())[0])
print(list(YY.items()))
print(list(YY.items())[0])
print("No.12 ######################  辞書型データの確認03です。 End ######################")

print("\nNo.13 ######################  importとfromの違いの確認です。 Start ######################")
print("#### import mathでmathライブラリを取り込む。")
import math
print("円周率=",math.pi)
print("No.13 ######################  importとfromの違いの確認です。 End  ######################")

print("\nNo.14 ######################  importとfromの違いの確認です。 Start ######################")
print("#### from os import pathでpathイブラリを取り込む。")
from os import path
print("カレントディレクトリ=",path.abspath('.'))
print("No.14 ######################  importとfromの違いの確認です。 End ######################")
