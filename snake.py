from turtle import Turtle

STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turt = []
        self.length = 3
        for num in range(3):
            self.turt.append(Turtle("square"))
            self.turt[num].penup()
            self.turt[num].color("white")
            self.turt[num].back(20 * num)
        self.head = self.turt[0]

    def move(self):
        for seg in range((self.length - 1), 0, -1):
            self.turt[seg].goto(self.turt[seg - 1].xcor(), self.turt[seg - 1].ycor())
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
