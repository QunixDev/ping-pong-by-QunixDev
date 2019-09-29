#Ping Pong made by @QunixDev

#https://twitter.com/QunixDev 
import turtle

wn = turtle.Screen()
wn.title("Ping pong by @QunixDev")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#paddle A "lopatica" is just on Croatian
lopatica_a = turtle.Turtle()
lopatica_a.speed(0)
lopatica_a.shape("square")
lopatica_a.color("white")
lopatica_a.shapesize(stretch_wid=5, stretch_len=1)
lopatica_a.penup()
lopatica_a.goto(-350, 0)

#paddle B, "lopatica" is just on Croatian
lopatica_b = turtle.Turtle()
lopatica_b.speed(0)
lopatica_b.shape("square")
lopatica_b.color("white")
lopatica_b.shapesize(stretch_wid=5, stretch_len=1)
lopatica_b.penup()
lopatica_b.goto(350, 0)
#https://twitter.com/QunixDev
#ball, "loptica" is just on Croatian
loptica = turtle.Turtle()
loptica.speed(0)
loptica.shape("square")
loptica.color("white")
loptica.penup()
loptica.goto(0, 0)
loptica.dx = 0.5
loptica.dy = 0.5

# pen the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#https://twitter.com/QunixDev
#functions
def lopatica_a_gore():
    y = lopatica_a.ycor()
    y += 20
    lopatica_a.sety(y)
    
def lopatica_a_dole():
    y = lopatica_a.ycor()
    y -= 20
    lopatica_a.sety(y)

def lopatica_b_gore():
    y = lopatica_b.ycor()
    y += 20
    lopatica_b.sety(y)
    
def lopatica_b_dole():
    y = lopatica_b.ycor()
    y -= 20
    lopatica_b.sety(y)

#Keyboard input
wn.listen()
wn.onkeypress(lopatica_a_gore,"w")
wn.onkeypress(lopatica_a_dole,"s")
wn.onkeypress(lopatica_b_gore,"Up")
wn.onkeypress(lopatica_b_dole,"Down")

#Main game loop
while True:
    wn.update()
    #move ball
    loptica.setx(loptica.xcor() + loptica.dx)
    loptica.sety(loptica.ycor() + loptica.dy)
#https://twitter.com/QunixDev
    #border check
    if loptica.ycor() > 290:
        loptica.sety(290)
        loptica.dy *= -1
        
    if loptica.ycor() < -290:
        loptica.sety(-290)
        loptica.dy *= -1
        
    if loptica.xcor() > 390:
        loptica.goto(0,0)
        loptica.dx *= -1
        score_a += 1
        loptica.dx = 0.5
        loptica.dy = 0.5
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    if loptica.xcor() < -390:
        loptica.goto(0,0)
        loptica.dx *= -1
        score_b += 1
        loptica.dx = 0.5
        loptica.dy = 0.5
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    #ball touching paddle
    if (loptica.xcor() > 340 and loptica.xcor() < 350) and (loptica.ycor() < lopatica_b.ycor() + 40 and loptica .ycor()> lopatica_b.ycor() - 40):
        loptica.setx(340)
        loptica.dx *= -1
        loptica.dx += 0.1
        loptica.dy += 0.1
    if (loptica.xcor() < -340 and loptica.xcor() > -350) and (loptica.ycor() < lopatica_a.ycor() + 40 and loptica .ycor()> lopatica_a.ycor() - 40):
        loptica.setx(-340)
        loptica.dx *= -1
        loptica.dx += 0.1
        loptica.dy += 0.1


    
    
