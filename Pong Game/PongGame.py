from turtle import Turtle,Screen
import time

class paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pos)
    def goup(self):
        self.goto(self.xcor(),self.ycor()+20)

    def godown(self):
        self.goto(self.xcor(),self.ycor()-20)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove=10
        self.ymove=10
    def ballmove(self):
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)
    def bouncey(self):
        self.ymove*=-1
    def bouncex(self):
        self.xmove*=-1
    def reset(self):
        self.goto(0,0)
        self.xmove=10
        self.ymove=10

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.updatescore()
    def updatescore(self):
        self.clear()
        self.goto(100,200)
        self.write(self.rscore,align="center",font=("Courier",80,"normal"))
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("Courier",80,"normal"))
    def lpoint(self):
        self.lscore+=1
        self.updatescore()
    def rpoint(self):
        self.rscore+=1
        self.updatescore()
    def gameover(self):
        self.goto(10,10)
        self.write("GAME OVER",align="center",font=("Courier",80,"normal"))


s=Screen()
s.bgcolor("black")
s.setup(width=800,height=600)
s.title("PONG!")
s.tracer(0)
rpaddle=paddle((350,0))
lpaddle=paddle((-350,0))

ball=Ball()

s.listen()
s.onkey(rpaddle.goup,"Up")
s.onkey(rpaddle.godown,"Down")
s.onkey(lpaddle.goup,"w")
s.onkey(lpaddle.godown,"s")

gameover=False
score=scoreboard()   
x=0.1
while not gameover:
    time.sleep(x)
    s.update()
    ball.ballmove()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    if(ball.distance(rpaddle) < 50 and ball.xcor() > 330 or ball.distance(lpaddle) < 50 and ball.xcor() < -330):
        ball.bouncex()
        x*=0.9
    if(ball.xcor()>360 ):
        ball.reset()
        score.lpoint()
        x=0.1
    if(ball.xcor()<-360):
        ball.reset() 
        score.rpoint() 
        x=0.1
    if(score.lscore ==10 or score.rscore ==10):
        gameover= True
        score.gameover()
        
s.exitonclick()
