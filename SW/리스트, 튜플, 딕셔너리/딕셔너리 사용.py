# 딕셔너리명[Key]
student1 = {'학번': 20520008, '이름': '김민경', '학과' : '클라우드융복합학과'}
print(student1['학번']) ## key로 value 접근 가능, 없는 key 호출 시 오류 발생

# 딕셔너리명.get(Key) 함수
print(student1.get('이름')) ## key로 value 접근 가능, 없는 key 호출하면 반환 값이 없음

# 딕셔너리의 모든 key들을 반환
print(student1.keys())

# 리스트 형태로 반환 가능
print(list(student1.keys()))

# 딕셔너리명.values() 함수
print(student1.values())

# list(딕셔너리명.values()) 함수
print(list(student1.values()))