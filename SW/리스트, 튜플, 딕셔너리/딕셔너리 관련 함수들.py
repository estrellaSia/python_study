# keys() - key 리스트 만들기
a = {'name':'mk', 'phone' : '010-1234-5678', 'birth' : '1112'}
print(a.keys()) # 결과값: dict_keys(['name', 'phone', 'birth'])

# values() - value 리스크 만들기
print(a.values()) # 결과값: dict_values(['mk', '010-1234-5678', '1112'])

# items() - key, value 쌍 얻기
print(a.items()) # 결과값: dict_items([('name', 'mk'), ('phone', '010-1234-5678'), ('birth', '1112')])