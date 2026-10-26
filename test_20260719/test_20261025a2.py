# FastAPIを利用したプログラムを作成する。
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    word1= "君島みお"
    word2= "さんが好きだ。"
    return {"Message1": word1, "Message2": word2}
#### 本アプリの起動の方法
## (1)Webサーバの起動方法
##    (bashやPowerShellの)コマンドプロンプトで以下のコマンドを実行する。
##   $ uvicorn test_20261025a2:app --reload
## (2)Webブラウザやcurlコマンドで以下のURLにアクセスする。
##    http://localhost:8000/
