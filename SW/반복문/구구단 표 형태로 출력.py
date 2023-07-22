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
