from utils import *


screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

t = turtle.Pen()
turtle.speed(10000)
turtle.hideturtle()
turtle.bgcolor('black')

# MAX size of triangle
A = (0, 0)
B = (700, 0)
C = (350, 606.22)

# fix centre
fix = (-350, -300)

A = (A[0] + fix[0], A[1] + fix[1])
B = (B[0] + fix[0], B[1] + fix[1])
C = (C[0] + fix[0], C[1] + fix[1])

edgeList = [A, B, C]
turtle.Turtle(visible=False)


def middle_point(point1, point2):
    x_mid = (point1[0] + point2[0]) / 2
    y_mid = (point1[1] + point2[1]) / 2
    point = (round(x_mid, 4), round(y_mid, 4))
    return point


r = random_point_in_triangle(A,B,C)
for i in range(3000):
    edge = random.choice(edgeList)
    r = middle_point(r, edge)
    draw_dot(r)

turtle.exitonclick()
