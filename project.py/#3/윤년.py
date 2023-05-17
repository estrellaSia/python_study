# 윤년인지 판단하는 프로그램
# 4로 나누어떨어지고, 100으로 나누어 떨어지지 않으면 윤년
# 400으로 나누어 떨어지는 해도 윤년

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")