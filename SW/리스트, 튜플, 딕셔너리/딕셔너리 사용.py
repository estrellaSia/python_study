# 딕셔너리명[Key]
student1 = {'학번': 20520008, '이름': '김민경', '학과' : '클라우드융복합학과'}
print(student1['학번']) ## key로 value 접근 가능, 없는 key 호출 시 오류 발생

# 딕셔너리명.get(Key) 함수
student1.get('이름') ## key로 value 접근 가능, 없는 key 호출하면 반환 값이 없음