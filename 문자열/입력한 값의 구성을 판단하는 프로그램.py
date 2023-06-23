# 입력한 값이
# 영어 or 한글이면 => '글자입니다'
# 숫자이면 => '숫자입니다'
# 섞여 있으면 => '글자+숫자입니다'
# 특수문자 등이면 => '모르겠습니다'
# 라고 출력되는 프로그램

str = input("문자열 입력 : ")

if str.isdigit() :
    print("숫자입니다.")
elif str.isalpha() :
    print("글자입니다.")
elif str.isalnum() :
    print("글자+숫자입니다.")
else :
    print("모르겠습니다.")