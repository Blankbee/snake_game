from hashlib import new
import time
import turtle
import random

score=0
hscore=0

spd=0.1

wn=turtle.Screen()
wn.title("Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

head=turtle.Turtle()
head.color("black")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.color("red")
food.shape("square")
food.penup()
x = random.randint(-14, 14)*20
y = random.randint(-14, 14)*20
food.goto(x,y)

tails=[]

wd = turtle.Turtle()
wd.speed(0)
wd.shape("square")
wd.color("white")
wd.penup()
wd.hideturtle()
wd.goto(0, 260)
wd.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

def up():
    if head.direction!="down":
        head.direction="up"
def down():
    if head.direction!="up":
        head.direction="down"
def right():
    if head.direction!="left":
        head.direction="right"
def left():
    if head.direction!="right":
        head.direction="left"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
def you_died():
    global score,spd
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    for tail in tails:
        tail.goto(1000,1000)
        
    tails.clear()
    score=0
    spd=0.1

    wd.clear()
    wd.write("Score: {}  High Score: {}".format(score, hscore), align="center", font=("Courier", 24, "normal"))
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        you_died()
    if head.distance(food)<20:
        x = random.randint(-14, 14)*20
        y = random.randint(-14, 14)*20
        food.goto(x,y)

        new_tail=turtle.Turtle()
        new_tail.color("grey")
        new_tail.shape("square")
        new_tail.penup()
        tails.append(new_tail)

        score+=10
        spd-=0.001

        if score>hscore:
            hscore=score
        wd.clear()
        wd.write("Score: {}  High Score: {}".format(score, hscore), align="center", font=("Courier", 24, "normal"))
    
    for index in range(len(tails)-1, 0, -1):
        x = tails[index-1].xcor()
        y = tails[index-1].ycor()
        tails[index].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)

    move()
    
    for tail in tails:
        if tail.distance(head)<20:
            you_died()
    time.sleep(spd)

