import turtle as t
t.speed(100)
size = 300
points = 100
angle = 180 - (180/points)

t.color("Dark red")
t.begin_fill()
for i in range(points):
    t.forward(size)
    t.right(angle)

t.end_fill()
input()