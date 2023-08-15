from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)] #파이썬에서 상수 이름은 모두 대문자를 씀
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #만약 이게 self.create_snake()보다 위에 있으면 에러, segemts가 비어있기 때문에
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:#아래쪽 방향이 아닌 경우에는 위쪽 방향으로 움직이는게 가능(현재 방향이 아래쪽이면, 위쪽으로 갈 수 x)
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
                self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)