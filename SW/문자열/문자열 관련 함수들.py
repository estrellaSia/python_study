# 문자 개수 세기 - count()
a = "hobby"
print(a.count('b')) # 결과값: 2

# 위치 알려 주기 - find()
s = "hello python!"
print(s.find('p')) # 결과값: 6

print(s.find('k')) # 결과값:  -1

# 위치 알려 주기 - index()
b = "Life is too short"
print(b.index('t')) # 결과값: 8

# 문자열 삽입 - join()
c = ",".join('abcd')
print(c) # 결과값: a,b,c,d

e = ",".join(['a', 'b', 'c', 'd'])
print(e) # 결과값: a,b,c,d

# 소문자를 대문자로 바꾸기 - upper()
d = "hello"
print(d.upper())

# 대문자를 소문자로 바꾸기 - lower()
f = "HI"
print(f.lower())