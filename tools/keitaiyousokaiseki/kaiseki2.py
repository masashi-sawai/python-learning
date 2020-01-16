# text-mining.py

# python解析器janomeをインポート - 1
from janome.tokenizer import Tokenizer

# 形態素解析用オブジェクトの生成 - 2
text = Tokenizer()

# txtファイルからデータの読み込み - 3
text_file = open("analyze_text.txt")
bindata = text_file.read()
txt = bindata

# txtから読み込んだデータを形態素解析 - 4
lines = txt.split("\r\n")
for i in lines:
    print(i)
    print("\n")
    text_c = text.tokenize(i)
    for j in text_c:
        print(j)

print("\n")

# テキストを一行ごとに処理 - 5
word_dic = {}
lines_1 = txt.split("\r\n")
print(lines_1)
print("\n")
for line in lines_1:
    malist = text.tokenize(line)
    for w in malist:
        word = w.surface
        ps = w.part_of_speech  # 品詞 - 6
        if ps.find("名詞") < 0:
            continue  # 名詞だけをカウント - 7
        if not word in word_dic:
            word_dic[word] = 0
        word_dic[word] += 1

# よく使われる単語を表示 - 8
keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
for word, cnt in keys[:50]:
    print("{0}({1}) ".format(word, cnt), end="")
