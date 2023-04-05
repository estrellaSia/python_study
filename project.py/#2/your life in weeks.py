# 90년을 산다고 가정했을 때,
# 나이를 입력하면 앞으로 살 날이 얼마나 남았는지 계산해주는 프로그램
# (1년은 365일, 52주, 12달이라고 가정)

age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining *12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)