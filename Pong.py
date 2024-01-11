import turtle
import tkinter
import winsound

# Funtion to move paddles
def leftPaddleUp():
    # if paddle is not at the border of y axis, then it can move upward
    if paddle_l.ycor() < 290:
        paddle_l.sety(paddle_l.ycor() + 20)

def leftPaddleDown():
    # if paddle is not at the border of y axis, then it can move downward
    if paddle_l.ycor() > -290:
        paddle_l.sety(paddle_l.ycor() - 20)

def rightPaddleUp():
    # if paddle is not at the border of y axis, then it can move upward
    if paddle_r.ycor() < 290:
        paddle_r.sety(paddle_r.ycor() + 20)

def rightPaddleDown():
    # if paddle is not at the border of y axis, then it can move downward
    if paddle_r.ycor() > -290:
        paddle_r.sety(paddle_r.ycor() - 20)

# Initiliaze a tkinter object to change the icon of turtle window from default to pong icon
root = tkinter.Tk()
# Give path of icon
root.iconbitmap("ping-pong.ico")
# Prevent the tkinter window from appearing
root.withdraw()

# Background window settings
window = turtle.Screen()
window.title("Pong! - By Hasan Mehdavi")
# Set the icon of turtle window to pong icon using root object which was of tkinter library
window._root.iconbitmap("ping-pong.ico")
window.bgcolor("blue")
window.setup(width=800, height=600)
# default speed of window
window.tracer(0)

# Keyboard bindings
window.listen()
window.onkeypress(leftPaddleUp, "w")
window.onkeypress(leftPaddleDown, "s")
window.onkeypress(rightPaddleUp, "Up")
window.onkeypress(rightPaddleDown, "Down")

# Paddle Left
paddle_l = turtle.Turtle()
paddle_l.shape("square")
paddle_l.speed(0)
paddle_l.color("red")
paddle_l.penup()
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.goto(-350, 0)

# Paddle Right
paddle_r = turtle.Turtle()
paddle_r.shape("square")
paddle_r.speed(0)
paddle_r.color("red")
paddle_r.penup()
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("red")
ball.penup()
# Set value of changes in x and y of ball.
ball.dx = 0.25
ball.dy = 0.25

# Score
score_left = 0
score_right = 0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Player A: {score_left} Player B: {score_right}", align="center", font=("Arial", 24, "normal"))

# Count bounces to increase the speed of ball if there are significant number of bounces
bounces = 0

# Main game loop
while True:
    window.update()

    # Move ball throughout the window
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # If hit the horizontal walls, then bounce.
    if ball.ycor() > 290:
        ball.dy *= -1
        winsound.PlaySound("wall_bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.dy *= -1
        winsound.PlaySound("wall_bounce.wav", winsound.SND_ASYNC)

    # If misses the paddles and hit the vertical walls:
    if ball.xcor() < -390:
        winsound.PlaySound("score_increase.wav", winsound.SND_ASYNC)
        # go to origin
        ball.goto(0, 0)
        # set bounces again to 0 for new round
        bounces = 0
        # set change in x and y to default
        ball.dx = 0.25
        ball.dy = 0.25
        # change direction of ball
        ball.dx *= -1
        # add score
        score_right += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {score_left} Player B: {score_right}", align="center", font=("Arial", 24, "normal"))

    if ball.xcor() > 390:
        winsound.PlaySound("score_increase.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        bounces = 0
        ball.dx = -0.25
        ball.dy = 0.25
        ball.dx *= -1
        score_left += 1
        scoreboard.clear()
        scoreboard.write(f"Player A: {score_left} Player B: {score_right}", align="center", font=("Arial", 24, "normal"))

    # If either player scores 10, the game ends.
    if score_left == 10:
        scoreboard.clear()
        scoreboard.write(f"Player A won!", align="center", font=("Arial", 24, "normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)
        turtle.ontimer(window.bye, 1000)
        ball.dy = 0
        ball.dx = 0

    if score_right == 10:
        scoreboard.clear()
        scoreboard.write(f"Player B won!", align="center", font=("Arial", 24, "normal"))
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)
        turtle.ontimer(window.bye, 2000)
        ball.dy = 0
        ball.dx = 0

    # If ball hits the paddles, then:
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() - 50:
        # Set x coordinate of ball to the left of the paddle so that it does not bounce in a wierd way.
        ball.setx(340)
        winsound.PlaySound("paddle_bounce.wav", winsound.SND_ASYNC)
        # change direction
        ball.dx *= -1
        # increase bounces
        bounces += 1
        # if bounces have reachen to a certain limit, increase the change in x and y to increase ball speed.
        if bounces % 3 == 0 and bounces != 0:
            if not ball.dx < -1:
                ball.dx -= 0.25
            if ball.dy > 0:
                ball.dy += 0.25
            else:
                ball.dy -= 0.25

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_l.ycor() + 50 and ball.ycor() > paddle_l.ycor() - 50:
        ball.setx(-340)
        winsound.PlaySound("paddle_bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1
        bounces += 1
        if bounces % 3 == 0 and bounces != 0:
            if not ball.dx + 0.25 > 1:
                ball.dx += 0.25
            if ball.dy > 0:
                ball.dy += 0.25
            else:
                ball.dy -= 0.25

