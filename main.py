from turtle import Turtle, Screen

brush = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    brush.forward(10)


def move_backward():
    brush.backward(10)


def rotate_clockwise():
    brush.right(10)


def rotate_counter_clockwise():
    brush.left(10)


def clear():
    brush.clear()
    brush.penup()
    brush.home()
    brush.pendown()


screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=rotate_clockwise, key="a")
screen.onkey(fun=rotate_counter_clockwise, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()

