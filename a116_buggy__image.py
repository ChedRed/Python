#   a116_buggy_image.py
import turtle as trtl

trtl.pensize(40)
trtl.circle(20)
legcount = 8
leglength = 70
legrotation = 360 / legcount

count = 0
trtl.pensize(5)
while (count < legcount):
  trtl.goto(0,0)
  trtl.setheading(legrotation*count)
  trtl.forward(leglength)
  count += 1
trtl.hideturtle()
wn = trtl.Screen()
wn.mainloop()
