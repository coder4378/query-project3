#space invaders 1st day
#player and screen
import turtle
import os
#set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
#space invaders 2nd day
#player movement
player_speed = 15
#move the player left
def move_left():
    x =player.xcor()
    x -=player_speed
    if x < -280:
     x = -280
     player.setx(x)
#move player right
def move_right():
    x =player.xcor()
    x +=player_speed
    if x > 280:
        x = 280
        player.setx(x)
    
#create key board bindings
#right key
turtle.listen()
turtle.onkey(move_left, "Left")
#left key
turtle.listen()
turtle.onkey(move_right, "Right")

