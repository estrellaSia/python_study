#문자열을 입력받아 그중 O을 $로 변경하는 문자열 변경하는 코드

ss = input("입력 문자열 ==> ")

print("출력 문자열 ==>", end = '')
for i in range(0, len(ss)):
    if ss[i] != 'o' :
        print(ss[i], end = '')
    else:
        print('$', end = '')