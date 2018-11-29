from wordcloud import WordCloud
import jieba

wc = WordCloud(
    background_color='white',
    font_path='C:\Windows\Fonts\STZHONGS.TTF',
    max_words=2000,
    max_font_size=150,
    random_state=30
)

line = """
上周，美国商务部工业安全署（BIS）出台了最新技术出口管制先期通知，并就这一框架方案向公众征询意见，这或将成为美国对技术出口最严的一次管制。根据这份框架，美国政府考虑对14个类别的科技关键领域进行管制，包括人工智能、芯片、量子计算、机器人、面印和声纹技术等被认为涉及国家安全和高技术的前沿科技。
"""
text = ''
text += ' '.join(jieba.cut(line, cut_all=False))

wc.generate(text)
# wc.to_file("文章.jpg")(前文词云代码)
wc.to_file("标题.jpg")
print('生成词云成功!')
