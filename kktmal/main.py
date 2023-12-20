import random

# 특정 글자로 시작하는 리스트 추출
def filter_words_starting_with(lst, prefix):
    return [word for word in lst if word.startswith(prefix)]

def errMessage(err_num):
    errList = {1 : "게임을 종료합니다",
               2 : "컴퓨터 승리\n게임을 종료합니다. \n이 게임에서 이미 사용된 단어입니다. ",
               3 : "컴퓨터 승리\n게임을 종료합니다. \n표준국어대사전에 등재된 단어 중 동사, 형용사, 속담, 관용구를 제외한 단어를 입력해주세요.",
               4 : "컴퓨터 승리 \n게임을 종료합니다. \n플레이어의 입력 값은 컴퓨터 입력 단어의 마지막 글자로 시작해야 합니다."}
    return errList[err_num]

#단어 목록 추출
word_list = []
word_list_file = "kktmal\\wordlist.txt"

with open(word_list_file, "r",encoding="utf-8") as f:
    example = f.read()

allstr = example
word_list = allstr.split('\n')
word_list.remove(word_list[-1])

used_word_list = []

#main
print("\n끝말잇기 v1.0\n\n끝말잇기의 단어 데이터는 2023.09.18의 표준국어대사전 등재 단어를 기준으로 합니다\n")

a = input("게임을 시작하려면 \"시작\"을 입력하세요\n단어를 추가하려면 \"단어추가\"를 입력하세요")
if a == "시작":
    print("──────────────────────────────────────────────────")
    print("게임 시작")
    gamestate = 1
    
    #컴퓨터 첫단어 고르기
    computer_choice = random.choice(word_list)
    used_word_list.append(computer_choice)
    word_list.remove(computer_choice)
    
    print("컴퓨터 : {0}\n".format(computer_choice))
    last_lett = computer_choice[-1]
    
    #플레이어 단어 입력
    player_choice = input("플레이어 : ")
    
    if player_choice[0] == last_lett: # 플레이어 단어가 컴퓨터 마지막단어와 같을때
        
        if player_choice in word_list: # 단어가 사전에 있을 때

            while gamestate == 1: #게임 반복 부분(플레이어 첫입력 마지막단어 검사 후~게임끝까지)
                last_lett = player_choice[-1]
                prefix_to_search = last_lett
                used_word_list.append(player_choice)
                word_list.remove(player_choice)
                
                result_list = filter_words_starting_with(word_list, prefix_to_search) #마지막글자로 시작하는 단어 리스트 반환
                if result_list != []:
                    computer_choice = random.choice(result_list) #컴퓨터 단어 선택
                    used_word_list.append(computer_choice)
                    word_list.remove(computer_choice)
                else:
                    print("플레이어 승리!")
                    gamestate = 2
                    break
                
                print("컴퓨터 : {0}\n".format(computer_choice))
                last_lett = computer_choice[-1]
                player_choice = input("플레이어 : ")
                
                if player_choice[0] == last_lett:
                    if player_choice in word_list:
                        continue
                    else:
                        gamestate = 0
                        if player_choice in used_word_list:
                            print(errMessage(2))
                        else:
                            print(errMessage(3))
                else:
                    gamestate = 0
                    print(errMessage(4))
                
        else:
            gaemstate = 0
            print(errMessage(3))
    elif a == "단어추가":
        pass
    else:
        gamestate = 0
        print(errMessage(4))
    
else:
    print(errMessage(1))
    
    #hi