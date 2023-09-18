# with 키워드 => 파일을 직접 관리, 우리가 일을 끝냈다는 것을 알아차리는 즉시 파일을 닫음

# 읽기 전용
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# w => write
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# a => append
with open("my_file.txt", mode="a") as file:
    file.write("\nHello")

# 파일 새로 생성
with open("new_file.txt", mode="a") as file:
    file.write("New Text.")