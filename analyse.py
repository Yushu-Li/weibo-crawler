import requests
from bs4 import BeautifulSoup
import jieba.analyse
import matplotlib.pyplot as plt
from PIL import Image, ImageSequence
import numpy as np
from wordcloud import WordCloud

import csv
#读取csv文件
name='三胎'
with open("./结果文件/"+name+"/"+name+".csv", "r") as f:
    with open ("./结果文件/"+name+"/"+name+".txt", "w") as f1:
        reader = csv.reader(f)
        for row in reader:
            f1.write(row[4])
            f1.write('\n')

coco = open("./结果文件/"+name+"/"+name+".txt", encoding="utf-8").read()  # 读取文件
result = jieba.analyse.textrank(coco, topK=50, withWeight=True)  # 词频分析
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)
wc = WordCloud(font_path='/Library/Fonts/Songti.ttc', background_color='White', max_words=50)
wc.generate_from_frequencies(keywords)
# image = Image.open('./reqiqiu.jpg')  # 生成云图，设置样式
# graph = np.array(image)
# wc = WordCloud(font_path='./fonts/simhei.ttf', background_color='White', max_words=50, mask=graph)
# wc.generate_from_frequencies(keywords)
# image_color = ImageColorGenerator(graph)
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file('./结果文件/'+name+'/'+name+'.png')