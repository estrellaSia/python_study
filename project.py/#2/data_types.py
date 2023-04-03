# 두 자리 숫자 입력 시 각 자리의 수를 더하는 프로그램

two_digit_number = input("Type a two digit number: ")

# type 확인
# print(type(two_digit_number))


first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)