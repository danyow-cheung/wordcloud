import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('data/word.txt','r',encoding= 'utf8').read()
# https://chinesefonts.org/fonts/source-han-sans-cn-light
font_path = 'han.otf'


# 产生词云
wordcloud = WordCloud(
font_path=font_path, 
).generate(text)

#原始大小的文字    
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# plt.savefig("output/noraml_wc.png")
