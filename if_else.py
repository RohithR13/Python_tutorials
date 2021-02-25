import turtle
r_t = turtle.Turtle()
def square():
    r_t.forward(100)
    r_t.right(90)
    r_t.forward(100)
    r_t.right(90)
    r_t.forward(100)
    r_t.right(90)
    r_t.forward(100)


elephant_weight = 3000
ant_weight = 0.1
if elephant_weight > ant_weight:
    square()
else:
    r_t.forward(100)    