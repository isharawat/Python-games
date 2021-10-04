#Game for single player

import turtle as t
playerAscore=5

window=t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=650)
window.tracer(0)

#creating paddle
paddle=t.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=5,stretch_wid=1)
paddle.penup()
paddle.goto(0,-290)

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
pen.write("Score: 5",align="center",font=("Arial",16,"normal"))


#moving the paddle
def paddleright():
    x=paddle.xcor()
    x=x+90
    paddle.setx(x)
    
def paddleleft():
    x=paddle.xcor()
    x=x-90
    paddle.setx(x)
    
#Assign keys to play

window.listen()
window.onkeypress(paddleleft,'Left')
window.onkeypress(paddleright,'Right')

while True:
    window.update()
    
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
    
    #setting borders for paddle
    if paddle.xcor()>360:
        paddle.setx(360)
    
    if paddle.xcor()<-360:
        paddle.setx(-360)
        
    #settingup border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
        
    if ball.ycor()<-300:
        playerAscore-=1;
        ball.goto(0,0)
        ballydirection=ballydirection*-1
        pen.clear()
        pen.write("Score:{}".format(playerAscore),align='center',font=("Arial",16,"normal"))
    
    if ball.xcor()>400:
        ball.setx(400)
        ballxdirection=ballxdirection*-1
        
    if ball.xcor()<-400:
        ball.setx(-400)
        ballxdirection=ballxdirection*-1
        
    #Handling the Collisions
    if(ball.ycor()<-290)and(ball.ycor()>-300)and(ball.xcor()>paddle.xcor()-45) and ball.xcor()<paddle.xcor()+45:
       ball.sety(-290)
       ballydirection=ballydirection*-1