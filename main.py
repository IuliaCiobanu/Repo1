from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle()
r_paddle.pad_position(350, 0)

l_paddle = Paddle()
l_paddle.pad_position(-350, 0)

screen.listen()
screen.onkey(key="Up", fun = r_paddle.move_up)
screen.onkey(key="Down", fun = r_paddle.move_down)

screen.onkey(key="a", fun = l_paddle.move_up)
screen.onkey(key="z", fun = l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 350:
        ball.reset()
        scoreboard.score_left()

    if ball.xcor() < -350:
        ball.reset()
        scoreboard.score_right()

screen.exitonclick()


# pt tema

# a="Mariana"
# b=3
# c=True
# d=1.70
#
# print(type(a), type(b), type(c), type(d))
#
# d=round(d)
# print(f"Numele ei este {a}")
# print("In fata sunt "+ str(b) + " brazi")
# print(f"Am verificat sa vedem daca este {c}")
# print(f"Dulapul avea o lungime de {d}m")

# nume=input("Numele ")
# prenume=input("Prenumele ")
# print(f"Numele complet are " +str(len(nume)+len(prenume)) +" caractere")

# lungimea=int(input("lungimea "))
# latimea=int(input("latimea "))
# print("Aria dreptunghiului este " + str(lungimea*latimea))

cora='Coral is either the stupidest animal or the smartest rock'
# z=cora.count("the")
# print(z)

# no=any(char.isdigit() for char in cora)
# print(type(no))

# cora='Coral is either the stupidest animal or the smartest rock'
# l=cora.isnumeric()
# assert l,"Nu sunt numai numere"

# def PrintMiddle(cuvant):
#     if len(cuvant)%2==0:
#         print("Mijlocul este''")
#     else:
#         middle = round( len( cuvant ) / 2 )
#         print(cuvant[middle])
# x=input("Alege un cuvant ")
# PrintMiddle(x)


# def check_palindrom(x):
#     # a=len(x)
#     for nr in range(0,len(x)-1):
#         assert x[nr]==x[len(x)-1-nr], "is not a palindrom"
#
# m=input("alege un cuvant")
# check_palindrom(m)

#  Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

# a=input("scrie ceva")