import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("red")
pen.speed(4)

# Function to draw a heart
def draw_heart():
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Draw the heart
draw_heart()


time.sleep(2)

# Move the turtle to a position to write text
pen.up()
pen.setpos(-100, -50)
pen.down()

# Write the message
pen.color("black")
pen.write("Hey there, cutie!", font=("Arial", 16, "bold"))

# Hide the turtle after drawing
pen.hideturtle()

# Finish
turtle.done()