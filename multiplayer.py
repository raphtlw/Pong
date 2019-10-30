import turtle

# window params
WIDTH = 900
HEIGHT = 600
wn = turtle.Screen()
wn.setup(WIDTH, HEIGHT)
wn.bgcolor('black')
wn.title('Pong by raphtlw')

# score
score1 = 0
score2 = 0

# game objects
# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.penup()
paddle_1.hideturtle()
paddle_1.color('white')
paddle_1.shape('square')
paddle_1.shapesize(6, 1)
paddle_1.speed(0)
paddle_1.goto(-400, 0)
paddle_1.showturtle()

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.penup()
paddle_2.hideturtle()
paddle_2.color('white')
paddle_2.shape('square')
paddle_2.shapesize(6, 1)
paddle_2.speed(0)
paddle_2.goto(400, 0)
paddle_2.showturtle()

# ball
ball = turtle.Turtle()
ball.penup()
ball.color('white')
ball.shape('circle')
ball.shapesize(0.7, 0.7)
ball.speed(0)
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A: 0  Player B: 0", align="center", font=("Inter", 24, "normal"))

# movement functions
pong_inc_ycor = 40
pong_ycor_limit = 210

def paddle_1_up():
    if paddle_1.ycor() > pong_ycor_limit:
        pass
    else:
        y = paddle_1.ycor()
        y += pong_inc_ycor
        paddle_1.sety(y)

def paddle_1_down():
    if paddle_1.ycor() < -pong_ycor_limit:
        pass
    else:
        y = paddle_1.ycor()
        y -= pong_inc_ycor
        paddle_1.sety(y)

def paddle_2_up():
    if paddle_2.ycor() > pong_ycor_limit:
        pass
    else:
        y = paddle_2.ycor()
        y += pong_inc_ycor
        paddle_2.sety(y)

def paddle_2_down():
    if paddle_2.ycor() < -pong_ycor_limit:
        pass
    else:
        y = paddle_2.ycor()
        y -= pong_inc_ycor
        paddle_2.sety(y)

# key binding
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

wn.listen()

while True:

    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball border checking
    # top and bottom
    top_bottom = 295
    if ball.ycor() > top_bottom:
        ball.sety(top_bottom)
        ball.dy *= -1
    elif ball.ycor() < -top_bottom:
        ball.sety(-top_bottom)
        ball.dy *= -1

    # ball speed increment
    ball_speed_inc = 0.7

    # left and right
    left_right = 440
    if ball.xcor() > left_right:
        score1 += 1
        pen.clear()
        pen.write("Player A: %s  Player B: %s" % (score1, score2), align="center", font=("Inter", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx -= ball_speed_inc
        ball.dy -= ball_speed_inc
    elif ball.xcor() < -left_right:
        score2 += 1
        pen.clear()
        pen.write("Player A: %s  Player B: %s" % (score1, score2), align="center", font=("Inter", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx += ball_speed_inc
        ball.dy += ball_speed_inc

    # pong and ball collisions
    pong_bounce_point = 380
    if ball.xcor() < -pong_bounce_point and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.dx *= -1
    elif ball.xcor() > pong_bounce_point and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.dx *= -1