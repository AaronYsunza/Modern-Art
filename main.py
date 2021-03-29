import turtle
import random


turtle.shape("circle")
turtle.speed(1000)

for i in range(50):
  red = random.randint(0, 255)
  green = random.randint(0, 255)
  blue = random.randint(0, 255)

  x = random.randint(-300, 300)
  y = random.randint(-300, 300)

  turtle.color(red, green, blue)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

  # Draw a rectangle
  # length and height to be random, between 10 and 100
  # fill in the color

  length = random.randint(10,100)
  height = random.randint(10,100)

  turtle.begin_fill()

  turtle.forward(length)
  turtle.right(90)
  turtle.forward(height)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(height)

  turtle.end_fill()

  radius = random.randint(10, 100)

  x2 = random.randint(-300, 300)
  y2 = random.randint(-300, 300)

  turtle.penup()
  turtle.goto(x2, y2)
  turtle.pendown()

  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()