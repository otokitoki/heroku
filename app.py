# -*- coding: utf-8 -*-
from flask import Flask, render_template 
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




@app.route('/hello')
def hello():
    name = "Hoge"
    return render_template('hello.html', name=name) 

@app.route('/rolling_ryu')
def rolling_ryu():
    
    return render_template('rolling_ryu.html') 

@app.route('/localStorage')
def localStorage():
    
    return render_template('localStorage.html') 

@app.route('/morsecode_translate')
def morsecode_translate():
    
    return render_template('morsecode_translate.html') 

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
