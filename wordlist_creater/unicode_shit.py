# print(ord("나")) #45208
# print(ord("닣")) #45795
# print(ord("라")) #46972
# print(ord("맇")) #47559

word_list = []
with open("kktmal\\chinese_lastword_list.txt", "r",encoding="utf-8") as f:
    example = f.read()

allstr = example
word_list = allstr.split('\n')
word_list.remove(word_list[-1])

f.close()

lastwordlist = []

k = open("kktmal\\two_sound_lastword_list.txt", 'w',encoding="UTF-8")
for i in word_list:
    word = i[0]
    if 45208 <= ord(word) <= 45795 or 46972 <= ord(word) <= 47559:
        lastwordlist.append(word)
        k.write(word + "\n")

k.close()