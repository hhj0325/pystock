from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import jieba

comments = []
with open('files/comments.txt', 'r', encoding='utf-8')as f:
    rows = f.readlines()
    try:
        for row in rows:
            comment = row.split(',')[2]
            if comment != '':
                comments.append(comment)
                # print(city)
    except Exception as e:
        print(e)
comment_after_split = jieba.cut(str(comments), cut_all=False)
words = ' '.join(comment_after_split)
# 多虑没用的停止词
stopwords = STOPWORDS.copy()
stopwords.add('电影')
stopwords.add('一部')
stopwords.add('一个')
stopwords.add('没有')
stopwords.add('什么')
stopwords.add('有点')
stopwords.add('感觉')
stopwords.add('毒液')
stopwords.add('就是')
stopwords.add('觉得')
wc = WordCloud(width=1024, height=768, background_color='white', font_path='STKAITI.TTF',
               stopwords=stopwords, max_font_size=400, random_state=50)
wc.generate_from_text(words)
plt.imshow(wc)
plt.axis('off')
plt.show()
