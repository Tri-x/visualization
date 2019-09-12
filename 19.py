#用Python形象化三万字报告关键词

from collections import * #可统计词频
from numpy import * # 可用于数据处理 需安装模块 cmd>pip install numpy
from jieba import * # 可用于分词 需安装模块 cmd>pip install jieba
from wordcloud import * #可用于词语直观化 需安装模块 cmd>pip install wordcloud
from PIL import Image #可用于处理图片 需安装模块 cmd>pip install Pillow
from matplotlib.pyplot import * #可用于图像展示 需安装模块 cmd>pip install matplotlib
figure=figure() #用来创建总画布的窗口

txt=open('19.txt') #打开文件
data=txt.read() #读取文件
print(len(data))
#词语处理
words=cut(data, cut_all=False) #精确分词
words_list=[]
remove_words=[u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',
              u'通常',u'如果',u'我们',u'需要',u'要',u'更加',u'（',u'）',u'一定',u'与',u'“',u'”'u'！',u'\t', u'\n',
              u'.',u':',u';'u'?',u',',u'_',u'"',u'〇',u'“',u'”'] #去除无意义字符,这里只是举个例,肯定除此外还有很多
                                                 # u'' 中的u防止中文乱码
for word in words:
    if word not in remove_words: #如果不在移除词语中
        words_list.append(word)  #该词添加到词语列表

#词频统计
word_counts=Counter(words_list) #对词语做词频统计
word_counts_top_10=word_counts.most_common(10) #获取前10最高频的字词
for top_word in word_counts_top_10:
	print('词语‘'+str(top_word[0])+'’出现'+str(top_word[1])+'次')

#词频展示
background=array(Image.open('map.png')) #背景数组化
word_config=WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', #设置字体格式
    mask=background,
    background_color='white',#设置背景图颜色
    max_words=len(words_list), #最多显示词数
    max_font_size=100,#字体最大值
    scale=8,#数值越大越清晰
    prefer_horizontal=1,#0~1 词语水平出现几率
    colormap='Reds' #字体颜色
	)

word_config.generate_from_frequencies(word_counts) #根据频率生成词云
imshow(word_config) #显示词云
axis('off')#关闭坐标轴
#去掉多余白边
figure.set_size_inches(1024/100,1024/100)
subplots_adjust(bottom=0.05,left=0,top=0.95,right=1)#bottom,left可以理解是图像左下角点的坐标,top,right可以理解为图像右上角点的坐标,这些值介于0~1
savefig('19.jpg',dpi=500)#储存图片 dpi越大越清晰
show() #显示图像

#如果觉得本视频有用，请素质三连支持一波！谢谢！
#BY TONYMOT