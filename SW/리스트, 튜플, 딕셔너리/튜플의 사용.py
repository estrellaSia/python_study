# 튜플에서 + 연산
tt1 = (10, 20, 30, 40)
print(tt1[0])
print(tt1[0] + tt1[1] + tt1[2])

# 튜플 범위에 접근
print(tt1[1:3])
print(tt1[1:])
print(tt1[:3])

# 튜플의 덧셈, 곱셈
tt2 = ('A', 'B')
print(tt1 + tt2)
print(tt2 * 3)

# 튜플(읽기 전용)의 항목 변경
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)