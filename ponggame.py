import turtle
import winsound

score_a = 0
score_b = 0

#display screen
win = turtle.Screen()
win.setup(800,600) #W & H
win.bgcolor("cadetblue4")
win.title("Pong game")
win.tracer(0)

#left paddle
left_padd = turtle.Turtle()
left_padd.speed(0)
left_padd.shape("square")
left_padd.color("white")
left_padd.shapesize(stretch_wid=5,stretch_len=1)
left_padd.penup()
left_padd.goto(-380,0)

#right paddle
right_padd = turtle.Turtle()
right_padd.speed(0)
right_padd.shape("square")
right_padd.color("white")
right_padd.shapesize(stretch_wid=5,stretch_len=1)
right_padd.penup()
right_padd.goto(380,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0.4
ball.dy = 0.4

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Ariel",24,"normal"))


#moving paddles

def left_padd_up():
    left_padd.sety(left_padd.ycor()+20)

def left_padd_down():
    left_padd.sety(left_padd.ycor()-20)

def right_padd_up():
    right_padd.sety(right_padd.ycor()+20)

def right_padd_down():
    right_padd.sety(right_padd.ycor()-20)

win.listen()
win.onkeypress(left_padd_up,'w')
win.onkeypress(left_padd_down, 's')
win.onkeypress(right_padd_up,'Up')
win.onkeypress(right_padd_down, 'Down')

while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #ball - wall collision
    #top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # right wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
    # left wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
    # Collision with Paddles
    if ball.xcor() > 370 and right_padd.ycor()-50 < ball.ycor() < right_padd.ycor()-50:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -370 and left_padd.ycor()-50 < ball.ycor() < left_padd.ycor()-50:
        bal.setx(-360)
        ball.dx *= -1
