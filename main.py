import turtle
import time

window = turtle.Screen()
window.title("hello world")
window.bgcolor("#111")

window.setup(width=800, height=600)
window.tracer(0)


square = turtle.Turtle()
square.color("#fff")
square.penup()
square.shape("square")
square.shapesize(stretch_len=1, stretch_wid=1)
square.goto(0, 0)

border_center = turtle.Turtle()
border_center.penup()
border_center.setposition(0, 0)
border_center.shape("square")
border_center.color("#fff")
border_center.shapesize(stretch_len=0.1, stretch_wid=25)

pall1, pall2 = 0, 0
score = turtle.Turtle()
score.penup()
score.color("#fff")
score.goto(0, 270)
score.hideturtle()
score.write(f"pall2: {pall2} , pall1: {pall1}", align="center", font={"san-serif", 20})


left_user = turtle.Turtle()
left_user.penup()
left_user.shape("square")
left_user.shapesize(stretch_len=1, stretch_wid=5)
left_user.color("red")
left_user.setx(-370)


right_user = turtle.Turtle()
right_user.penup()
right_user.shape("square")
right_user.shapesize(stretch_len=1, stretch_wid=5)
right_user.color("blue")
right_user.setx(370)


pally, pallx = 1, 1
speed_sq = 0.5




def up_pall1():
    if right_user.ycor() < 240:
        right_user.sety(right_user.ycor() + 20)
    else:
        return


def down_pall1():
    if right_user.ycor() > -240:
        right_user.sety(right_user.ycor() - 20)
    else:
        return


def up_pall2():
    if left_user.ycor() < 240:
        left_user.sety(left_user.ycor() + 20)
    else:
        return


def down_pall2():
    if left_user.ycor() > -240:
        left_user.sety(left_user.ycor() - 20)
    else:
        return


turtle.listen()
turtle.onkeypress(up_pall1, "Up")
turtle.onkeypress(down_pall1, "Down")

turtle.onkeypress(up_pall2, "t")
turtle.onkeypress(up_pall2, "T")
turtle.onkeypress(down_pall2, "b")
turtle.onkeypress(down_pall2, "B")


while True:
    window.update()

    square.goto(square.xcor() + pallx * speed_sq, square.ycor() + pally * speed_sq)

    if square.xcor() > 380:
        square.goto(0, 0)
        pallx *= -1
        pall1 += 263
        score.clear()
        score.write(f"pall2: {pall2} , pall1: {pall1}", align="center", font={"san-serif", 20})
        # print(pallx)

    if square.xcor() < -380:
        square.goto(0, 0)
        pallx *= -1
        pall1 += 1
        score.clear()
        score.write(f"pall2: {pall2} , pall1: {pall1}", align="center", font={"san-serif", 20})
        # print(pallx)

    if square.ycor() > 280:
        square.sety(280)
        pally *= -1
    if square.xcor() > 380:
        square.setx(380)
        pallx *= -1

    if square.ycor() < -280:
        square.sety(-280)
        pally *= -1
    if square.xcor() < -380:
        square.setx(-380)
        pallx *= -1

    if (
        square.xcor() > 350
        and square.xcor() < 360
        and square.ycor() > (right_user.ycor() - 60)
        and square.ycor() < (right_user.ycor() + 60)
    ):

        square.setx(350)
        pallx *= -1

    if (
        square.xcor() < -350
        and square.xcor() > -360
        and square.ycor() > (left_user.ycor() - 60)
        and square.ycor() < (left_user.ycor() + 60)
    ):

        print(square.xcor())
        square.setx(-350)
        pallx *= -1
