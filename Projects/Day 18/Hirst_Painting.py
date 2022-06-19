import turtle as t
import random

color_list = [(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15)]


def random_color():
    color = random.choice(color_list)
    return color


t.colormode(255)

hirst = t.Turtle()
screen = t.Screen()
hirst.speed("fastest")

x_as = -200
y_as = -200
hirst.penup()
hirst.setpos(x_as, y_as)
hirst.hideturtle()

for column in range(10):
    for row in range(10):
        hirst.dot(20, random_color())
        hirst.penup()
        x_as += 50
        hirst.setpos(x_as, y_as)
    row = 0
    x_as = -200
    y_as += 50
    hirst.setpos(x_as, y_as)


screen.exitonclick()
