import turtle
import random

s=turtle.Screen()

t1=turtle.Turtle()
t1.color("pink")
t1.shape("turtle")

t2=turtle.Turtle()
t2.color("blue")
t2.shape("turtle")

t1.up()
t1.goto(-400,100)
t1.down()

t2.up()
t2.goto(-400,-100)
t2.down()

def start():
    for _ in range(50):
        d1=random.randint(1,30)
        t1.fd(d1)
    
        d2=random.randint(1,30)
        t2.fd(d2)

    print(t1.position())
    print(t2.position())

s.onkey(start,"Up")
s.listen()


