#   a116_ladybug.py
import turtle as trtl

#   Setup and run loop
count = 0
trtl.pensize(5)
while (count < 6):

  # Draw legs
  trtl.goto(0,-35)
  trtl.setheading(((int(count/3)%2)*60)+((240/6)*count)-40)
  trtl.forward(55)
  count += 1

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55)
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = xpos + 5
  ypos = ypos + 25
  num_dots += 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()
