# 1 ~ 5까지 저장된 리스트
numList = []
for num in range(1, 6):
    numList.append(num)
print(numList)

# 컴프리헨션으로 작성
numList = [num for num in range(1, 6)]
print(numList)

numList = [num * num for num in range(1, 6)]
print(numList)