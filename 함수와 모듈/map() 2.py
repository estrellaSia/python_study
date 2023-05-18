list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

myList = list(map(lambda num1, num2 : num1 + num2, list1, list2))
print(myList)
