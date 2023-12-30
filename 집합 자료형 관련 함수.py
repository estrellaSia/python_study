# add() - 값 1개 추가하기
s1  = set([1,2,3])
s1.add(4)
print(s1) # 결과값: {1, 2, 3, 4}

# update() - 값 여러 개 추가하기
s1  = set([1,2,3])
s1.update([4, 5, 6])
print(s1) # 결과값: {1, 2, 3, 4, 5, 6}

# remove() - 특정 값 제거하기
s1  = set([1,2,3])
s1.remove(2)
print(s1)