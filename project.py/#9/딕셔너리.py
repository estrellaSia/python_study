programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.", 
} # dictionary는 종종 이렇게 정렬함(마지막에 '}' 표시)


# Value 가져오기
print(programming_dictionary["Bug"])

# 존재하지 않는 key를 넣으면=> 키 에러 발생
print(programming_dictionary["ljpjuh"])

# 새로운 항목 추가
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# 빈 딕셔너리 생성
empty_dictionary = {}

# 이미 존재하는 딕셔너리 지우기
programming_dictionary = {}
print(programming_dictionary)

# 딕셔너리 안의 값 수정하기
programming_dictionary["Bug"] = "A moth in your computer."

# 딕셔너리로 반복문을 사용할 때 매우 유용함
for key in programming_dictionary:
  print(key) # key출력
  print(programming_dictionary[key]) # 그 key에 해당하는 value 출력