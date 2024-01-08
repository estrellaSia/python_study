# 메모리 => 컴퓨터가 프로그램에서 사용하는 데이터를 기억하는 공간

a = [1, 2, 3]
b = id(a)
print(b)

# copy 모듈 이용하기
from copy import copy
a = [1, 2, 3]
c = copy(a)
print(c)