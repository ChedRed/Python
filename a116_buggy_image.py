#   a116_buggy_image.py
import turtle as trtl


#   Using 'trtl' as the painter ¯\_(ツ)_/¯
#   Draw spider head and body
trtl.pensize(40)
trtl.circle(20)
trtl.goto(0,-80)
trtl.pensize(40)
trtl.circle(40)


#   Setup variables for spider
legcount = 8
leglength = 70
legrotation = 280 / legcount


#   Setup and run loop
count = 0
trtl.pensize(5)
while (count < legcount):


  # Draw legs
  trtl.penup()
  trtl.goto(0,20)
  trtl.pendown()
  trtl.setheading((legrotation*count)-((int(count/4)%2)*245))
  trtl.circle(leglength+((3.5-abs(count-3.5))*10), (((int(count/4)%2)-0.5)*2)*120)
  count += 1


# Eyes :D
trtl.color(1,1,1)
trtl.penup()
trtl.goto(-10,40)
trtl.pendown()
trtl.circle(5)
trtl.penup()
trtl.goto(17,40)
trtl.pendown()
trtl.circle(5)


#   Cleanup and display
trtl.hideturtle()
wn = trtl.Screen()
wn.mainloop()
