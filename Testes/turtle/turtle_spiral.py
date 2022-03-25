import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
for x in range(1000):
    t.pencolor(colors[x%6])
    t.width(x//1000 + 1)
    t.forward(5 + x/10)
    t.right(15)