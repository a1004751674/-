import django
from django.test import TestCase
from matplotlib.pyplot import title
import pandas as pd
from polls import models
# Create your tests here.

import PIL.Image as Image
import jieba
import jieba.analyse
import numpy
import pandas as pd
import xlwt  # 写入Excel表的库
from snownlp import SnowNLP
from wordcloud import WordCloud

def importData():#导入数据
    models.Newsdata.objects.all().delete()
    data = pd.read_csv("./pachongdata.csv")
    data1 = data.to_dict('records')
    for i in data1:
        models.Newsdata.objects.create(title=i['title'],media=i['newssource'],time=i['dt'],content=i['article'],MediaScr = i['pictrue'])
    models.Newsdata.objects.filter(MediaScr='nan').all().update(MediaScr='')
importData()

     
def exportData():
        with open("data_title.txt", 'w') as file:
            file.truncate(0)
        with open("data_article.txt", 'w') as file:
            file.truncate(0)
        data1=list(models.Newsdata.objects.all().values())
        for text in data1:
            if text['title'] is not None:
                with open('data_title.txt', mode='a', encoding='utf-8') as file:
                    file.write(str(text['title'])+"\n")
            if text['content'] is not None:
                with open('data_article.txt', mode='a', encoding='utf-8') as file:
                    file.write(str(text['content'])+"\n")
        print('写入title.txt完成!')
        print('写入article.txt完成!')

exportData()

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def fenci_title():
    #题目
    inputs = open('data_title.txt', 'r', encoding='utf-8')
    outputs = open('标题分词数据.txt', 'w', encoding='utf-8')
    for line in inputs:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()
 
def fenci_content():
#内容
    inputs = open('data_article.txt', 'r', encoding='utf-8')
    outputs = open('内容分词数据.txt', 'w', encoding='utf-8')
    for line in inputs:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()


def cut(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=" ".join(wordlist_jieba)
    return space_wordlist

###制作标题词云
def ciyun_title():
    with open(r"标题分词数据.txt" ,encoding="utf-8")as file:
        text=file.read()
        text=cut(text)
        mask_pic=numpy.array(Image.open(r"python.png"))
        wordcloud = WordCloud(font_path=r"仿宋_GB2312.ttf",
        collocations=False,
        max_words= 100,
        min_font_size=10,
        max_font_size=100,
        mask=mask_pic).generate(text)
        image=wordcloud.to_image()
        image.show()
        wordcloud.to_file('标题词云图.png')  # 把词云保存下来
        
ciyun_title()

###制作内容词云
def ciyun_content():
    with open(r"内容分词数据.txt" ,encoding="utf-8")as file:
        text=file.read()
        text=cut(text)
        mask_pic=numpy.array(Image.open(r"python.png"))
        wordcloud = WordCloud(font_path=r"仿宋_GB2312.ttf",
        collocations=False,
        max_words= 100,
        min_font_size=10,
        max_font_size=100,
        mask=mask_pic).generate(text)
        image=wordcloud.to_image()
        image.show()
        wordcloud.to_file('内容词云图.png')  # 把词云保存下来
        
ciyun_content()

###标题分词统计
def count_title():

    wbk = xlwt.Workbook(encoding='ascii')
    sheet = wbk.add_sheet("wordCount")  # Excel单元格名字
    word_lst = []
    key_list = []
    for line in open('data_title.txt', encoding='utf-8'):  # 需要分词统计的原始目标文档

        item = line.strip('\n\r').split('\t')  # 制表格切分
        # print item
        tags = jieba.analyse.extract_tags(item[0])  # jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict = {}
    with open("标题分词统计.txt", 'w') as wf2:  # 指定生成文件的名称

        for item in word_lst:
            if item not in word_dict:  # 统计数量
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        orderList = list(word_dict.values())
        orderList.sort(reverse=True)
        # print(orderList)
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key] == orderList[i]:
                    wf2.write(key + ' ' + str(word_dict[key]) + '\n')  # 写入txt文档
                    key_list.append(key)
                    word_dict[key] = 0

    for i in range(len(key_list)):
        sheet.write(i, 1, label=orderList[i])
        sheet.write(i, 0, label=key_list[i])
    wbk.save('标题词频统计.xls')

count_title()

###内容分词统计
def count_content():

    wbk = xlwt.Workbook(encoding='ascii')
    sheet = wbk.add_sheet("wordCount")  # Excel单元格名字
    word_lst = []
    key_list = []
    for line in open('data_article.txt', encoding='utf-8'):  # 需要分词统计的原始目标文档

        item = line.strip('\n\r').split('\t')  # 制表格切分
        # print item
        tags = jieba.analyse.extract_tags(item[0])  # jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict = {}
    with open("内容分词统计.txt", 'w') as wf2:  # 指定生成文件的名称

        for item in word_lst:
            if item not in word_dict:  # 统计数量
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        orderList = list(word_dict.values())
        orderList.sort(reverse=True)
        # print(orderList)
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key] == orderList[i]:
                    wf2.write(key + ' ' + str(word_dict[key]) + '\n')  # 写入txt文档
                    key_list.append(key)
                    word_dict[key] = 0

    for i in range(len(key_list)):
        sheet.write(i, 1, label=orderList[i])
        sheet.write(i, 0, label=key_list[i])
    wbk.save('内容词频统计.xls')

count_content()



def importCount_title():
    models.frequencytitle.objects.all().delete()
    df = pd.read_excel('.\标题词频统计.xls',sheet_name='wordCount')
    data = df.to_dict('records')
    first = list(data[1].keys())
    models.frequencytitle.objects.create(word=first[0],frequency=first[1])
    for i in data:
        models.frequencytitle.objects.create(word=i[first[0]],frequency=i[first[1]])
importCount_title()

def importCount_content():
    models.frequencycontent.objects.all().delete()
    df = pd.read_excel('.\内容词频统计.xls',sheet_name='wordCount')
    data = df.to_dict('records')
    first = list(data[1].keys())
    models.frequencycontent.objects.create(word=first[0],frequency=first[1])
    for i in data:
        models.frequencycontent.objects.create(word=i[first[0]],frequency=i[first[1]])
importCount_content()