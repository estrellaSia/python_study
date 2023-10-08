# readlines() : 파일 안에 있는 모든 줄을 리스트 형태로 반환
# replace() : 특정 구문을 구체적으로 명시된 다른 구문으로 바꿈
# strip() : 문자열 앞과 뒤의 공백을 지워줌

PLACEHOLDER = "[name]"

# 상대경로로 현재 'Mail Merge Project Start'를 불러오고 Input->Names->invited_names.txt 파일 열기
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)