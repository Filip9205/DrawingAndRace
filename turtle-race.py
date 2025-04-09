from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -240
y = 130
mark = 0

racers = []

for racer in colors:
    new_racer = Turtle(shape="turtle")
    new_racer.penup()
    new_racer.color(colors[mark])
    new_racer.goto(x=x, y=y)
    racers.append(new_racer)
    y -= 50
    mark += 1

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 215:
            is_race_on = False
            print(f"{racer.color()[0].capitalize()} turtle have won the race")
            if user_bet == racer.color()[0]:
                print("You have won!")
            else:
                print("You have lost!")
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)

screen.exitonclick()
