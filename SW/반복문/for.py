# 0과 100 사이에 있는 7의 배수 합계 구하기
i, hap = 0,0

for i in range(0, 101, 7) :
    hap = hap + i

print("0과 100 사이에 있는 7의 배수 합계: %d" %hap)


# 500~1000 사이에 있는 홀수의 합계를 구하는 포르그램
i, hap = 0, 0


for i in range(501, 1001, 2) :
    hap = hap + i

print("500과 1000 사이에 있는 홀수의 합계 : %d" %hap)


# 1 ~ 사용자가 입력한 수까지의 합계
i, hap = 0, 0
num = 0

num = int(input("값을 입력하세요 : ")) 


for i in range(1, num+1, 1) :
    hap = hap + i

print("1에서 %d까지의 합계 : %d" %(num, hap))


#시작값, 끝값, 증가값을 사용자에게 입력받는 프로그램
i, hap = 0, 0
num1, num2, num3 = 0, 0, 0

num1 = int(input("시작값을 입력하세요 : "))
num2 = int(input("끝값을 입력하세요 : "))
num3 = int(input("증가값을 입력하세요 : "))

for i in range(num1, num2 + 1, num3) :
    hap = hap + i

print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" % (num1, num2, num3, hap))

