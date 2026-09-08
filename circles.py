import turtle

t = turtle.Pen()
color = ["red", "blue", "yellow", "green"]

for x in range(150):
    t.pencolor(color[x%4])
    t.circle(x)
    t.left(91)
turtle.done()