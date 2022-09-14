import turtle

# screen attributes
win = turtle.Screen()
win.title("Pong Tutorial")
win.bgcolor('black')
win.setup(width=800, height=600)

win.tracer(0) # something to do with screen refresh

# ball attributes
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# paddle attributes
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(360,0)

# functions
def paddle_a_up():
    if ball.dx < 0:
        y = paddle_a.ycor()
        y += 30
        paddle_a.sety(y)

def paddle_a_down():
    if ball.dx < 0:
        y = paddle_a.ycor()
        y -= 30
        paddle_a.sety(y)

def paddle_b_up():
    if ball.dx > 0:
        y = paddle_b.ycor()
        y += 30
        paddle_b.sety(y)

def paddle_b_down():
    if ball.dx > 0:
        y = paddle_b.ycor()
        y -= 30
        paddle_b.sety(y)

# inputs
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# game loop
run = True
while run:
    # ball starting movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## border interactions
    # ball
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= -1
    
    # paddles
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # paddle interactions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle_b.ycor() + 50) and ball.ycor() > (paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (paddle_a.ycor() + 50) and ball.ycor() > (paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1

    win.update()