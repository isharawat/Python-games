#Simple Python game
import turtle as t
import time
import random

delay=0.1
#score
score=0
high_score=0

#Set up the screen
window = t.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates

#Snake head
head=t.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="up"

#object 
obj=t.Turtle()
obj.speed(0)
obj.shape("circle")
obj.color("red")
obj.penup()
obj.goto(0,100)

#Setting the snake body
segments=[]

#Showing Score and high Score
pen=t.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: {}   High Score: {}".format(score,high_score),align="center",font=("Arial",20))

#functions for movement
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
#Fucntion to change snake's direction
def go_up():
    if head.direction!="down":
       head.direction="up"

def go_down():
    if head.direction!="up":
       head.direction="down"

def go_left():
    if head.direction!="right":
       head.direction="left"

def go_right():
    if head.direction!="left":
        head.direction="right"

#Assigning the keys for changing direction
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")
   
#main game loop
while True:
    window.update()
    
    #check for collision
    if head.distance(obj)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        obj.goto(x,y)
        
        #Add a segment
        new_segment=t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        #Increase the score 
        score+=5
        high_score=max(score, high_score)
        
        #Showing scores
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score,high_score),align="center",font=("Arial",20))
               
    #move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        
    #moving along the borders
    if head.xcor()>300:
        head.setx(-300)
    if head.xcor()<-300:
        head.setx(300)
    if head.ycor()>300:
        head.sety(-300) 
    if head.ycor()<-300:
        head.sety(300)                  
    move()
    
    #collision with itself
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            #Reset the scores
            score=0
            head.direction="stop"
          
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            
    time.sleep(delay)


window.mainloop()