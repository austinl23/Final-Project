import turtle
import time
import random


delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
area = turtle.Screen()
area.bgcolor("slategrey")
area.setup(width=460, height=700)

# juul pod 
juul = turtle.Turtle()
juul.speed(0)
juul.shape("square")
juul.color("black")
juul.penup()
juul.goto(0,0)
juul.direction = "stop"

# Snake device
device = turtle.Turtle()
device.speed(0)
device.shape("square")
device.color("orange")
device.penup()
device.goto(100,100)

juulcase = []


# Juul Body juulbodys 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write("Score: 0  High Score: 0", align="center", font=("Comic Sans", 24, "normal"))

pen.goto(0, 260)
pen.write("Use W, A, S, D Keys to PLAY".format(score, high_score), align="center", font=("Comic Sans", 8, "normal")) 


''' This set of functions is the overall movement of the game wich allows the 
juul to go up and down side to side and at the bottom is the code for how the 
keys respond to the direction '''

# Juul Main Controles
def go_down():
    if juul.direction != "up":
        juul.direction = "down"

def go_up():
    if juul.direction != "down":
        juul.direction = "up"

def go_right():
    if juul.direction != "left":
        juul.direction = "right"

def go_left():
    if juul.direction != "right":
        juul.direction = "left"

''' This is the function that allows the juul case to stay center and attach to the juul pod allowying for no gaps'''

def move():
    if juul.direction == "up":
        y = juul.ycor()
        juul.sety(y + 20)

    if juul.direction == "down":
        y = juul.ycor()
        juul.sety(y - 20)

    if juul.direction == "left":
        x = juul.xcor()
        juul.setx(x - 20)

    if juul.direction == "right":
        x = juul.xcor()
        juul.setx(x + 20)

''' This is the keys so if you press on the keybord it moves the juul '''

# Keyboard Controls 
area.listen()
area.onkeypress(go_up, "w")
area.onkeypress(go_down, "s")
area.onkeypress(go_left, "a")
area.onkeypress(go_right, "d")

# Juul Main Brains
while True:
    area.update()

    # Check for a collision with the border
    if juul.xcor()>200 or juul.xcor()<-200 or juul.ycor()>320 or juul.ycor()<-320:
        time.sleep(1)
        juul.goto(0,0)
        juul.direction = "stop"

        # Hide the juulcase
        for juulbody in juulcase:
            juulbody.goto(1000, 1000)
        
        # Clear the Juul after hitting the walls
        juulcase.clear()

        # score goes to 0
        score = 0

        # Juuls Delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans", 24, "normal")) 

        
    # Juul Collision
    if juul.distance(device) < 20:
        
        x = random.randint(-190, 190)
        y = random.randint(-190, 190)
        device.goto(x,y)

    
        
        # Add body of juul
        new_juulbody = turtle.Turtle()
        new_juulbody.speed(0)
        new_juulbody.shape("square")
        new_juulbody.color("silver")
        new_juulbody.penup()
        juulcase.append(new_juulbody)

        
        
        delay -= 0.001

        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans", 24, "normal")) 

        
    # Juul Case 
    for index in range(len(juulcase)-1, 0, -1):
        x = juulcase[index-1].xcor()
        y = juulcase[index-1].ycor()
        juulcase[index].goto(x, y)

    # Move Juul 0 to where the juul is
    if len(juulcase) > 0:
        x = juul.xcor()
        y = juul.ycor()
        juulcase[0].goto(x,y)

    move()    

    # Check for juul collision with the body juulcase
    for juulbody in juulcase:
        if juulbody.distance(juul) < 20:
            time.sleep(1)
            juul.goto(0,0)
            juul.direction = "stop"
        
            # Hide the juulcase
            for juulbody in juulcase:
                juulbody.goto(1000, 1000)
        
            # Clear the juulcase list once a colison 
            juulcase.clear()

            # Reset the score after running into self
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Score updater
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Comic Sans", 24, "normal"))

    time.sleep(delay)

area.mainloop()

