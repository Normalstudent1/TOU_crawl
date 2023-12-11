word_list = []
with open("wordlist.txt", "r",encoding="utf-8") as f:
    example = f.read()

allstr = example
word_list = allstr.split('\n')
word_list.remove(word_list[-1])

f.close()

firstwordlist = []

k = open("firstword_list.txt", 'w',encoding="UTF-8")
for i in word_list:
    print(i[0])
    word = i[0]
    k.write(word + "\n")

k.close()