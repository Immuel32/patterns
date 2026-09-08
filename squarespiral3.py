import turtle

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "blue", "yellow", "green"]

for x in range(300):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(93)
turtle.done()