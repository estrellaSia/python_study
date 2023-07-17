import random

# 1 ~ 10까지의 정수 생성
random_integer = random.randint(1, 10)
print(random_integer)

# 0.000.. ~ 9.999... 까지의 난수 생성
random_float = random.random()
print(random_float)

# 0.000... ~ 4.9999.. 까지의 난수 생성
randomFloat = random.random() * 5
print(randomFloat)