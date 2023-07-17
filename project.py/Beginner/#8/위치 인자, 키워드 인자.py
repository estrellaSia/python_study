#Functions with more than 1 input
#위치 인자
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")


#Funcions with keyword arguments
#키워드 인자
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with(location = "Nowhere", name = "Jack Bauer")