# -*- coding: utf-8 -*-
from flask import Flask
from pykakasi import kakasi as ka

app = Flask(__name__)

@app.route('/')
def index():

    text = "形態素解析sann"

    # オブジェクトをインスタンス化
    kakasi = ka()
    # モードの設定：J(Kanji) to H(Hiragana)
    kakasi.setMode('J', 'H') 

    # 変換して出力
    conv = kakasi.getConverter()
    text2 = conv.do(text)
    return text2

if __name__ == '__main__':
    app.run()
