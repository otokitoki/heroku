# -*- coding: utf-8 -*-
from flask import Flask, render_template 
from pykakasi import kakasi as ka

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route('/')
def index():
    name = "Hoge"
    return render_template('hello.html', name=name) 



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
