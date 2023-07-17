# 1 ~ 100 중에서 짝수들의 합 구하기

# method 1
total = 0
for number in range(2, 101, 2):
  total += number
print(total)

# method 2
total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total2 += number
print(total2)