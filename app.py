from django.shortcuts import render
import numpy as np
import sys
from flask import Flask, request, jsonify, render_template, redirect, url_for
from PIL import Image
import wikipedia
from wordcloud import WordCloud
import os
from os import path
import matplotlib.pyplot as plt
from analysci import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#生成词云主页面
@app.route('/wcg', methods=["POST","GET"])
def wcg():
    if request.method == "POST":
        
        words = request.form["words"]


        
        height = request.form["height"]
        width = request.form["width"]
        minfontsize = request.form["minfontsize"]
        maxfontsize = request.form["maxfontsize"]
        
        width = int(width)
        height = int(height)
        minfontsize = int(minfontsize)
        maxfontsize = int(maxfontsize)


        print(words)
        
        with open('data/content.txt','w') as f:
            f.write(words)  
        
        main()

        text = open('data/word.txt','r',encoding= 'utf8').read()
        font_path = 'han.otf'
    
        background = np.array(Image.open("cloud.png"))
    
        # 产生词云
        wc = WordCloud(
                    background_color="black",    
                    width = width,
                    min_font_size = minfontsize,
                    max_font_size = maxfontsize,
                    height = height,
                    mask = background,
                    font_path=font_path, 
                    stopwords = "stop_words.utf8"
                )
        wc.generate(text)

        wc.to_file("output/wordcloud.png")

        filename = Image.open("output/wordcloud.png")
        filename.show()
        
        return render_template('wcg.html')
    else:
        return render_template('wcg.html')

#小组成员
@app.route('/blog')
def blog():
    return render_template('blog.html')

#成果展示
@app.route("/table")
def table():
    return render_template("table.html")
if __name__ == "__main__":
    app.run(debug=True)
