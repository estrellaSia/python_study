# PROJECT 2
# 팁 계산기

# 지불할 전체 $124.56 중에서 12%를 팁으로 줄 것인데, 이 팁을 7명이서 나누어 내기
# 단 최종 답은 소수 둘째짜리로 반올림되게!

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")