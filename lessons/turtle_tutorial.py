from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-230, -130)
leo.pendown()

colormode(255)
leo.fillcolor("pink")
leo.pencolor("blue")


leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(500)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()

bob.speed(70)

bob.color("black")

bob.penup()
bob.goto(-230, -180)
leo.pendown()

side_length: int = 600
bob.begin_fill()
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
bob.end_fill()
side_length: int = 600

bob.fillcolor("black")

i: int = 0
while (i < 60):
    bob.forward(side_length)
    bob.left(121)
    i = i + 1
    side_length = int(side_length * 0.97)

done()
