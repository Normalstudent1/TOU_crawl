word_list = []
with open("kktmal\한자어.txt", "r",encoding="utf-8") as f:
    example = f.read()

allstr = example
word_list = allstr.split('\n')
word_list.remove(word_list[-1])

f.close()

lastwordlist = []

k = open("kktmal\chinese_lastword_list.txt", 'w',encoding="UTF-8")
for i in word_list:
    print(i[-1])
    word = i[-1]
    if word not in lastwordlist:
        lastwordlist.append(word)
        k.write(word + "\n")

k.close()