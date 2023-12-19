# keys() - key 리스트 만들기
a = {'name':'mk', 'phone' : '010-1234-5678', 'birth' : '1112'}
print(a.keys()) # 결과값: dict_keys(['name', 'phone', 'birth'])

# values() - value 리스크 만들기
print(a.values()) # 결과값: dict_values(['mk', '010-1234-5678', '1112'])

# items() - key, value 쌍 얻기
print(a.items()) # 결과값: dict_items([('name', 'mk'), ('phone', '010-1234-5678'), ('birth', '1112')])

# clear() - key:value 쌍 모두 지우기
print(a.clear()) # 결과값: None

# get() - key로 value 얻기
b = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(b.get('name')) # 결과값: pey
print(b.get('phone')) # 결과값: 010-9999-1234

# in() - 해당 key가 딕셔너리 안에 있는지 조사하기
b = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
c = 'name' in b
print(c) # 결과값: True