import turtle as t
import colorsys

t.bgcolor("black")
t.pencolor("cyan")
t.hideturtle()
t.tracer(2)

def AjCoding():
    for i in range(4):
        t.fd(200)
        t.right(90)

for j in range(500):
    AjCoding()
    t.goto(0,0)
    t.rt(2)


t.exitonclick()