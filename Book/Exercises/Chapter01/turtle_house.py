import turtle

t = turtle.Turtle()
t.speed(3)

# Draw square base
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw roof
t.left(45)
t.forward(70)
t.right(90)
t.forward(70)

turtle.done()