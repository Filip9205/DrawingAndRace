from turtle import Turtle, Screen

timmy = Turtle()


def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_right():
    timmy.right(5)


def turn_left():
    timmy.left(5)


def clear():
    timmy.reset()


screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
