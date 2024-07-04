import random
import turtle
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "black",
    "white",
    "pink",
    "brown",
    "cyan",
    "magenta",
    "lime",
    "gray",
    "gold",
    "silver",
    "maroon",
    "navy",
    "olive",
    "teal"
]


def random_point_in_triangle(A, B, C):
    # Step 1: Generate two random numbers
    u, v = random.random(), random.random()

    if u + v > 1:
        u, v = 1 - u, 1 - v

    # Step 3: Compute the point using the barycentric coordinates
    x = (1 - u - v) * A[0] + u * B[0] + v * C[0]
    y = (1 - u - v) * A[1] + u * B[1] + v * C[1]

    return (x, y)

def draw_line(point1, point2):
    turtle.penup()
    turtle.goto(point1)
    turtle.pendown()
    turtle.goto(point2)
    turtle.hideturtle()


def draw_dot(point):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(point)
    turtle.pendown()
    # nice colouring but too slow
    #distanceFromCentre = math.sqrt(pow(int(point[0]), 2) + pow(int(point[1]), 2))
    #turtle.dot(3, colors[int(distanceFromCentre / 23)])
    turtle.dot(3, colors[random.randint(0, 19)])
    turtle.hideturtle()
