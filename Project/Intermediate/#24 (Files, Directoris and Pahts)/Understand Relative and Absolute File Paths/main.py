# Relative Path (상대경로)
## 현재 작업 중인 디렉토리와 관련이 있음
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Absolute Paths (절대경로)
## 언제나 루트와 관련이 있음
with open("/Users/minky/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
