# 여러 이름을 입력하면 누가 계산할지 뽑아주는 프로그램

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")