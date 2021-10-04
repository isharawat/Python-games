# Ping Pong Game for two player
import turtle as t
playerAscore=0
playerBscore=0

#setting the display
window=t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(5,5)
ballxdirection=0.5;
ballydirection=0.5;

#creating pen for scoreboard update

pen=t.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,230)
pen.write("Score\n",align="center",font=("Arial",24,"normal"))

pen1=t.Turtle()
pen1.speed(0)
pen1.color("White")
pen1.penup()
pen1.hideturtle()
pen1.goto(0,220)
#moving the leftpaddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)
    
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)
    
#moving the rightpaddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)
    
def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)
    
#Assign keys to play

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')


while True:
    window.update()
    
    if playerAscore==5:
        pen.color(black)
        window.color(white)
        ball.color(white)
        pen.write("Player A wins the game",align='center',font=("Arial",16,"normal"))
        break
        
    if playerBscore==5:
         pen.color(black)
         window.color(white)
         ball.color(white)
         pen.write("Player B wins the game",align='center',font=("Arial",16,"normal"))
         break
         
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
    
    #settingup border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerAscore+=1
        pen1.clear()
        pen1.write("player A:{}     player B:{}".format(playerAscore,playerBscore),align='center',font=("Arial",16,"normal"))
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerBscore+=1
        pen1.clear()
        pen1.write("player A:{}     player B:{}".format(playerAscore,playerBscore),align='center',font=("Arial",16,"normal"))
        
    #Handling the Collisions
    
    if(ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+45) and ball.ycor()>rightpaddle.ycor()-45:
       ball.setx(340)
       ballxdirection=ballxdirection*-1
    
    if(ball.xcor()<-340)and(ball.xcor()>-350)and(ball.ycor()<leftpaddle.ycor()+45) and ball.ycor()>leftpaddle.ycor()-45:    
       ball.setx(-340)
       ballxdirection=ballxdirection*-1