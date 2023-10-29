# 딕셔너리 생성
dic1 = {1:'a', 2:'b', 3:'c'}
print(dic1)

# 딕셔너리 생성 (키와 값을 반대로 생성)
dic2 = {'a': 1, 'b': 2, 'c' : 3}
print(dic2)

# 딕셔너리 생성 (여러 정보를 하나의 변수로 표현할 때 유용함)
student1 = {'학번' : 20520008, '이름' : '김민경', '학과' : '클라우드융복합학과'}
print(student1)

# 딕셔너리에 쌍을 추가
student1['연락처'] = '010-1234-1234'
print(student1)

# 딕셔너리의 값을 변경
student1['학과'] = '아동가족복지학과'
print(student1)

# 딕셔너리의 쌍을 삭제
del(student1['학과'])
print(student1)