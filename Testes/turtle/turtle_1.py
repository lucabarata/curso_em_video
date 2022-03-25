import turtle

t = turtle.Turtle()


def dir():
    t.setheading(0)  # EAST
    t.forward(50)


def esq():
    t.setheading(180)  # WEST
    t.forward(50)


def cima():
    t.setheading(90)  # NORTH
    t.forward(50)


def baixo():
    t.setheading(270)  # SOUTH
    t.forward(50)


def penup():
    t.penup()


def circ():
    t.circle(50, 90)


def pula():
    t.setheading(90)
    t.forward(10)
    for c in range(15):
        t.forward(5)
        t.right(10)


while True:
    x = str(input('Para que direção deseja andar? (WASD)')).upper().strip()[0]
    if x == "D":
        dir()
    if x == "A":
        esq()
    if x == "W":
        cima()
    if x == "S":
        baixo()
    if x == "F":
        penup()
    if x == "G":
        t.pendown()
    if x == "C":
        circ()
    if x == "X":
        pula()

    if x not in "DAWSFGCX":
        print("Opção inválida.")
        break
