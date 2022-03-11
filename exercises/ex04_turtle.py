"""Drawing a house with sun and stick figures."""
__author__ = "730358329"

from random import randint
from turtle import Turtle, done, tracer, update


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    a_turtle: Turtle = Turtle()
    draw_rectangle(a_turtle, -10, 80, 150, 50, "black", "brown")
    draw_rectangle(a_turtle, 10, -20, 40, 60, "black", "blue")
    draw_rectangle(a_turtle, -360, -120, 710, 80, "green", "green")
    b_turtle: Turtle = Turtle()
    draw_circle(b_turtle, 20, -90, 10, "black", "black")
    c_turtle: Turtle = Turtle()
    draw_half_circle(c_turtle, -360, 220, 150, 180, "yellow", "yellow")
    d_turtle: Turtle = Turtle()
    draw_triangle(d_turtle, -55, 80, 195, "black", "brown")
    e_turtle: Turtle = Turtle()
    draw_person(e_turtle, randint(-300, 300), randint(-300, 300), 10, 40, "black")
    update() 
    done()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float, pen_color: str, fill_color: str) -> None:
    """Draw two rectangles, one that makes up the body of the house and another for the door."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.pencolor(pen_color)
    a_turtle.fillcolor(fill_color)
    i: int = 0
    a_turtle.begin_fill()
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(height)
        i = i + 1
    a_turtle.end_fill()


def draw_circle(b_turtle: Turtle, x: float, y: float, r: float, pen_color: str, fill_color: str) -> None:  
    """Draw a small circle on the door to represent the door knob."""
    b_turtle.penup()
    b_turtle.goto(x, y)
    b_turtle.setheading(0.0)
    b_turtle.pendown()
    b_turtle.pencolor(pen_color)
    b_turtle.fillcolor(fill_color)
    b_turtle.begin_fill()
    b_turtle.circle(r)
    b_turtle.end_fill()


def draw_half_circle(c_turtle: Turtle, x: float, y: float, r: float, extent: float, pen_color: str, fill_color: str) -> None:  
    """Draw half a circle on the top left corner of the page to represent the sun."""
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.setheading(0.0)
    c_turtle.pendown()
    c_turtle.pencolor(pen_color)
    c_turtle.fillcolor(fill_color)
    c_turtle.begin_fill()
    c_turtle.circle(r, extent)
    c_turtle.end_fill()


def draw_triangle(d_turtle: Turtle, x: float, y: float, width: float, pen_color: str, fill_color: str) -> None: 
    """Draw a triangle on top of the house to represent the roof."""
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.setheading(0.0)
    d_turtle.pendown()
    d_turtle.pencolor(pen_color)
    d_turtle.fillcolor(fill_color)
    i: int = 0
    d_turtle.begin_fill()
    while i < 3: 
        d_turtle.forward(width)
        d_turtle.left(120)
        i = i + 1
    d_turtle.end_fill()
    

def draw_person(e_turtle: Turtle, x: float, y: float, r: float, length: float, pen_color: str) -> None:
    """Draw a randomly generated number of stick figures in randomly generated places on the drawing."""
    e_turtle.penup()
    e_turtle.goto(x, y)
    e_turtle.setheading(0.0)
    e_turtle.pendown()
    e_turtle.pencolor(pen_color)
    i: int = 0
    n: int = randint(3, 10)
    while i < n:
        e_turtle.circle(r)
        e_turtle.right(90)
        e_turtle.forward(length)
        e_turtle.right(45)
        e_turtle.forward(length)
        e_turtle.backward(length)
        e_turtle.left(135)
        e_turtle.forward(length)
        i = i + 1
        random: int = randint(1, 200)
        x = x + float(random)
        y = y + float(random)
        e_turtle.penup()
        e_turtle.goto(x, y)
        e_turtle.pendown()


if __name__ == "__main__":
    main()
