import turtle
import time
import random
import pygame

speed = 0.1

score = 0
high_score = 0

#Playing Area
area = turtle.Screen()
area.bgcolor("teal")
area.setup(height=800, width=800)

#Juul Pod
juul = turtle.Turtle()
juul.shape("square")
juul.color("black")
juul.penup()
juul.direction = "stop"

#Juul Device
device = turtle.Turtle()
device.shape("square")
device.color("yellow")
device.penup()
device.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#Game
def move_down():
   if juul.direction != "up":
       juul.direction = "down"

def move_up():
   if juul.direction != "down":
       juul.direction = "up"

def move_right():
   if juul.direction != "left":
       juul.direction = "right"

def move_left():
   if juul.direction != "right":
       juul.direction = "left"
       

#Controls

area.listen()
area.onkeypress(move_down, "s")
area.onkeypress(move_up, "w")
area.onkeypress(move_left, "a")
area.onkeypress(move_right, "d")


def move():
    if juul.direction == "up":
        y = juul.ycor()
        juul.sety(y + 15)

    if juul.direction == "down":
        y = juul.ycor()
        juul.sety(y - 15)

    if juul.direction == "left":    
        x = juul.xcor()
        juul.setx(x - 15)

    if juul.direction == "right":
        x = juul.xcor()
        juul.setx(x + 15)

while True:
   
    area.update()

    if juul.xcor()>380 or juul.xcor()<-380 or juul.ycor()>380 or juul.ycor()<-380:
        time.sleep(1)
        juul.goto(0, 0)
        juul.direction = "stop"

    for segment in segments:
         segment.goto(1000, 1000)

    segments.clear()

    score = 0

    delay = 0.1

    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
   
    move()
   
    time.sleep(speed)
  
    if juul.distance(device) < 25:
        #move food
        x = random.randint(-380, 380)
        y = random.randint(-380, 380)
        device.goto(x,y)

    # Body Grrowing
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.shape("square")
        new_segments.color("red")
        new_segments.penup()
        segments.append(new_segments)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score; {}" .format(score, high_score), align="center", font=("Courier", 24, "normal"))



    #more body
    for index in range(len(segments)-3, 0, -3):
        x = segments[index-3].xcor()
        y = segments[index-3].ycor()
        segments[index].goto(x, y)
    
    if len(segments) > 0:
        x = juul.xcor()
        y = juul.ycor()
        segments[0].goto(x,y)
    
    move()

    for segment in segments:
        if segment.distance(juul) <20:
            time.sleep(1)
            juul.goto(0,0)
            juul.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score; {}" .format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)




area.mainloop()