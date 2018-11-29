from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import pandas as pd
import jieba

df = pd.read_csv('sg_articles.csv', header=None, names=["title", "article", "name", "date"])

text = ''
# for line in df['article'].astype(str):(前文词云代码)
for line in df['title']:
    text += ' '.join(jieba.cut(line, cut_all=False))
backgroud_Image = plt.imread('python_logo.jpg')
wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=2000,
    max_font_size=150,
    random_state=30
)
wc.generate_from_text(text)
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
# wc.to_file("文章.jpg")(前文词云代码)
wc.to_file("标题.jpg")
print('生成词云成功!')
