import random
import turtle
import time

delay = 0.1
score = 0
high_score = 0

s = turtle.Screen()
s.setup(650, 650)
s.title("My Turtle Program")
s.bgcolor("gray")

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.speed(1)
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"

s.listen()
s.onkey(go_up, "Up")
s.onkey(go_down, "Down")
s.onkey(go_left, "Left")
s.onkey(go_right, "Right")

def movement():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

food_position = food.pos()

body = []

text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: 0", align="center", font=("Courier", 24, "normal"))

while True:
    s.update()

    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        for i in body:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = "stop"
        body.clear()
        score = 0
        print("Game Over")
        break

    if snake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        food_position = food.pos()
        print(food_position)
        increase_snake = turtle.Turtle()
        increase_snake.shape("square")
        increase_snake.color("green")
        increase_snake.penup()
        increase_snake.goto(0, 0)
        increase_snake.speed(0)
        body.append(increase_snake)
        score += 10
        if score > high_score:
            high_score = score
            text.clear()
            text.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    movement()
    for i in body:
        if i.distance(snake) < 20:
            time.sleep(1)
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            snake.direction = "stop"
            body.clear()
            score = 0
            print("Game Over")
            break
    time.sleep(delay)

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

turtle.done()