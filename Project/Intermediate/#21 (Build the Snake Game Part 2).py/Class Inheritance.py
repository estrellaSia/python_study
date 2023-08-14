class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal): #객체가 상위에 있는 Animal 클래스의 '모든' 속성과 메소드를 물려받음
    def __init__(self):
        super().__init__() #상위 클래스를 상속하는 방법

    def breathe(self):
        super().breathe()
        print("doing this unerwater.") #breathe 메소드에 별도로 추가해준 부분(상위 클래스 + a)

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breathe()