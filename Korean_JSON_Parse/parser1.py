import json

f = open("wordlist.txt", 'w',encoding="UTF-8")

def write(data, i): # 메모장에 데이터 작성
    wordlist = []
    for i in range(i):
        if data["channel"]["item"][i]["word_info"]["pos_info"][0]["pos"] != "동사": #특정 품사의 단어 제거
            if data["channel"]["item"][i]["word_info"]["pos_info"][0]["pos"] != "형용사":
                if data["channel"]["item"][i]["word_info"]["pos_info"][0]["pos"] != "구":
                    global json_string
                    json_string = data["channel"]["item"][i]["word_info"]["word"]
                else:
                    pass

        if "-" in json_string: #문자열 내의 특정 문자 제거
            json_string = json_string.replace('-', '') 
        else:
            pass
        if "^" in json_string: 
            json_string = json_string.replace('^', '') 
        else:
            pass
        if " " in json_string: 
            json_string = json_string.replace(' ', '') 
        else:
            pass

        for k in range(11): # 문자열 안에 숫자가 포함되어있으면 숫자 제거
            if str(k) in json_string: 
                json_string = json_string.replace(str(k), '') 
            
        if json_string in wordlist: 
            pass
        else:
            if len(json_string) >= 2:
                wordlist.append(json_string) 
                f.write(json_string + "\n") 
                print(json_string) 
             

for i in range(1, 87):
    with open('C:\\Users\\calvi\\OneDrive\\바탕 화면\\코딩\\Korean_JSON_Parse\\전체 내려받기_표준국어대사전_JSON_20230906\\1200922_{0}.json'.format(str(i*5000)), 'rt', encoding="UTF-8") as json_file:
        json_data = json.load(json_file)

    write(json_data, 5000)

with open('C:\\Users\\calvi\\OneDrive\\바탕 화면\\코딩\\Korean_JSON_Parse\\전체 내려받기_표준국어대사전_JSON_20230906\\1200922_434361.json', 'rt', encoding="UTF-8") as json_file:
    json_data = json.load(json_file)

write(json_data, 4340)

f.close()