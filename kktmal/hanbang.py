# 파일 경로 설정
file_path = "kktmal\\wordlist.txt"  # 파일 경로를 실제 파일 경로로 바꿔주세요

# 빈 리스트 생성
first_characters = []
last_characters = []

# 파일 열기
with open(file_path, 'r', encoding='utf-8') as file:
    # 각 행의 첫 글자 추출하여 리스트에 추가
    for line in file:
        first_character = line.strip()[0]  # 각 행의 첫 글자 추출
        first_characters.append(first_character)

# 중복된 요소를 제거하고 유일한 값만 남기기 위해 set 사용
unique_first_characters = list(set(first_characters))

# 결과 출력
print(unique_first_characters)

file.close()

with open(file_path, 'r', encoding='utf-8') as file:
	for line in file:
		last_character = line.strip()[-1]  # 각 행의 맨 끝 글자 추출
		last_characters.append(last_character)

unique_last_characters = list(set(last_characters))
print(unique_last_characters)

# unique_last_characters 중 unique_first_characters에 없는 글자 추출
difference_characters = [char for char in unique_last_characters if char not in unique_first_characters]

# 결과 출력
print(difference_characters)

# 결과를 hanbang.txt 파일에 저장
output_file_path = "kktmal\\hanbang.txt"  # 결과를 저장할 파일 경로를 설정하세요

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for char in difference_characters:
        output_file.write(char + '\n')

print(f"결과가 {output_file_path} 파일에 저장되었습니다.")