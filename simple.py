from PIL import Image
from jieba import *
from numpy import *
from matplotlib.pyplot import *
from wordcloud import *
from collections import *
figure=figure()
data=open('19.txt').read()
words=cut(data,cut_all=False)
remove_words=[u'\n',u'\t',u'。',u'，',u'、',u'的',u'和']#还有更多无意义词汇 这里只是举例
words_list=[]
for word in words :
  if word not in remove_words:
    words_list.append(word)
words_counts=Counter(words_list)
word_top10=words_counts.most_common(10)
for word_top in word_top10:
  print(str(word_top[0]),str(word_top[1]))
background=array(Image.open('map.png'))
words_config=WordCloud(mask=background,scale=8,prefer_horizontal=1,max_font_size=100,max_words=len(words_list),colormap='Reds',font_path='C:/Windows/Fonts/simhei.ttf',background_color='white')
words_config.generate_from_frequencies(words_counts)
imshow(words_config)
axis('off')
figure.set_size_inches(1024/100,1024/100)
subplots_adjust(bottom=0.05,top=0.95,right=1,left=0)
savefig('19.jpg',dpi=500)
show()

如果觉得本视频有用，请素质三连支持一波！谢谢！
BY TONYMOT