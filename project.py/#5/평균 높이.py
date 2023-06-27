student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 아래부터 len(), sum() 사용 X
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

numbers_of_students = 0
for student in student_heights:
    numbers_of_students += 1        #for 반복문 ==> 리스트 내부의 항목 수만큼 반복 수행
print(f"number of students = {numbers_of_students}")

average_height = round(total_height / numbers_of_students)
print(average_height)
