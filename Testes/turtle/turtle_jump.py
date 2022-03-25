import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(1)
n = 36
h = 0
for i in range(10000):
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.color(c)
    t.forward(100)
    t.setposition(10, 10)
    t.setposition(20, 20)
    t.setposition(30, 30)