from turtle import *

speed(3)
pensize(10)
colormode(255)


penup()
goto(0, -100)
pendown()
fillcolor(37, 150, 190)
begin_fill()
circle(100)
end_fill()


penup()
goto(0, -100)
pendown()
pencolor(139, 117, 0)
circle(100)


penup()
pensize(2)
goto(-50, 130)
setheading(270)
pendown()
fillcolor(255, 215, 0)
pencolor(255, 255, 224)
begin_fill()
forward(260)
left(90)
forward(140)
left(90)
forward(30)
left(90)
forward(100)
right(90)
forward(230)
left(90)
forward(40)
end_fill()


bgcolor(20, 20, 20)

hideturtle()
done()
