import turtle
r_t = turtle.Turtle()
r_t.speed(5)
def square():
    r_t.forward(100)
    r_t.right(90)
    r_t.forward(100)
    r_t.right(90)
    r_t.forward(100)
    r_t.right(90)
    r_t.forward(100)
x = int(input("no. of square:"))
for i in range(x):
    square()
    r_t.forward(10 + 4*i)
    if i%2== 0:
        r_t.circle(i*2)
