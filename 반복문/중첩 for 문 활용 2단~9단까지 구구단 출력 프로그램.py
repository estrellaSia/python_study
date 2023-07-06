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