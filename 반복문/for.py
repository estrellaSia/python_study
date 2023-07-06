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

# 사용자가 입력한 숫자의 단에서 구구단을 출력하는 프로그램
i, dan = 0, 0

dan = int(input("단을 입력하세요 : "))

for i in range(1, 10, 1) :
    print("%d X %d = %2d" % (dan, i, dan*i))
    

# 사용자가 입력한 숫자의 단에서 구구단을 거꾸로 출력하는 프로그램
i, dan = 0, 0

dan = int(input("단을 입력하세요 : "))

for i in range(9, 0, -1) :
    print("%d X %d = %2d" % (i, dan, dan*i))
    
    
# 중첩 for 문 활용 2단~9단까지 구구단 출력 프로그램
i, k = 0, 0

for i in range(2, 10, 1) :
    for k in range(1, 10, 1) :
        print("%d X %d = %2d" %(i, k, i*k))
    print("")


# 중첩 for 문 활용 2단~9단까지 구구단 출력 프로그램-각 단의 제목 출력
i, k = 0, 0

for i in range(2, 10, 1) :
    print ("## %d단 ## " % i)
    for k in range(1, 10, 1) :
        print("%d X %d = %2d" %(i, k, i*k))
    print("")


#구구단 표형태로 출력하는 프로그램
i, k, guguLine = 0, 0, ""

for i in range(2, 10) :
    guguLine = guguLine + (" #  %d단  #" %i)

print(guguLine)

for i in range(1, 10) :
    guguLine = ""
    for k in range(2,10) :
        guguLine = guguLine + str("%2dX %2d= %2d" % (k, i, k*i))
    print(guguLine)
    

#구구단 표형태로 거꾸로 출력하는 프로그램
i, k, guguLine = 0, 0, ""

for i in range(9, 1, -1) :
    guguLine = guguLine + (" #  %d단  #" %i)

print(guguLine)

for i in range(9, 0, -1) :
    guguLine = ""
    for k in range(9, 1, -1) :
        guguLine = guguLine + str("%2dX %2d= %2d" % (k, i, k*i))
    print(guguLine)
