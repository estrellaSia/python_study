# 문자열이 괄호로 감싸 있지 않으면 괄호로 감싸주는 프로그램

ss = input("입력 문자열 ==> ")

if ss.startswith('(') == False :
    print("(", end = '')
    
print(ss, end = '')

if ss.endswith(')') == False :
    print(")", end = '')