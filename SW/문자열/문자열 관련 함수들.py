# 문자 개수 세기 - count()
a = "hobby"
print(a.count('b'))

# 위치 알려 주기 - find()
s = "hello python!"
print(s.find('p'))

print(s.find('k')) # 해당 문자가 없다면 -1을 반환

# 위치 알려 주기 - index()
b = "Life is too short"
print(b.index('t'))

# 문자열 삽입 - join()
print(",".join('abcd'))