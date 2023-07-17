###########DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21): #range(1,20)으로 설정시 오류!
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #randint(1, 6)로 설정 시 오류!
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: # year > 1994로 설정 시 1994는 포함되지 않아 오류!
  print("You are a Gen Z.")

#Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.") #들여쓰기 하지 않으면 오류!
# IndentationError: expected an indented block=> 들여쓰기(indentation) 오류


#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) 
  #word_per_page == int(input("Number of words per page: ")) (X)
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) #들여쓰기 해야 '[2, 4, 6, 10, 16, 26]'가 출력됨
  print(b_list)

mutate([1,2,3,5,8,13])