piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_keys[:5]) # a ~ e까지 출력됨
print(piano_keys[2:5]) # c, d, e가 출력됨
print(piano_keys[2:5:2]) # c, e가 출력됨
print(piano_keys[::5]) # a, c, e, g가 출력됨
print(piano_keys[::-1]) # ['g', 'f', 'e', 'd', 'c', 'b', 'a']가 출력됨

print(piano_tuple[2:5]) # ('mi', 'fa', 'so')가 출력됨