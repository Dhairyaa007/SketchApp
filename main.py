from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def move_upwards():
   new_heading = t.heading() + 10
   t.setheading(new_heading)


def move_downwards():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.penup()
    t.clear()
    t.home()
    t.pendown()


s.listen()
s.onkey(move_forwards, "d")
s.onkey(move_backwards, "a")
s.onkey(move_upwards, "w")
s.onkey(move_downwards, "s")
s.onkey(clear, "space")
s.exitonclick()
