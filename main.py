from turtle import Turtle, Screen

timmy1 = Turtle()
timmy2 = Turtle()
timmy1.shape("turtle")
timmy2.shape("turtle")

i = 0
for i in range(0, 12):
    timmy1.color("green")
    timmy2.color("coral")
    timmy1.forward(100)
    timmy2.forward(100)
    timmy1.right(30)
    timmy2.left(30)





myscreen = Screen()
myscreen.exitonclick()