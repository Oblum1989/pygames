import random
import turtle

s = turtle.Screen()
s.title("My Turtle Program")

t1 = turtle.Turtle()
t1.hideturtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(500, 200)
t1.pendown()
t1.circle(40)
t1.penup()
t1.goto(-500, 240)
t1.pendown()
t1.showturtle()

t2 = turtle.Turtle()
t2.hideturtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(500, -200)
t2.pendown()
t2.circle(40)
t2.penup()
t2.goto(-500, -160)
t2.pendown()
t2.showturtle()

dado = [1, 2, 3, 4, 5, 6]

for i in range(4):
    if t1.pos() >= (500, 240):
        print("Turtle 1 won")
        break
    elif t2.pos() >= (500, -160):
        print("Turtle 2 won")
        break
    else:
        input("Press enter to continue")
        turno1 = random.choice(dado)
        print("Turtle 1: ", turno1)
        t1.forward(100 * turno1)

        turno2 = random.choice(dado)
        print("Turtle 2: ", turno2)
        t2.forward(100 * turno2)

turtle.done()
