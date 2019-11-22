import turtle
import time
import random

d = 0.1

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
device.goto(0, 200)

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
   
    move()
   
    time.sleep(d)
  
    if juul.distance(device) < 9:
        #move food
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        device.goto(x,y)
        


area.mainloop()