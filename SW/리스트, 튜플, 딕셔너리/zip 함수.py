# zip() 함수 : 동시에 여러 리스트에 접근가능함

foods = ['떡볶이', '짜장면', '라면', '피자', '삼겹살']
sides = ['오뎅', '단무지', '김치']
tupList = list(zip(foods, sides))
dic = dict(zip(foods, sides))

print(tupList)
print(dic)