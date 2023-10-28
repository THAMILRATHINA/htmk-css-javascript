"""import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Move the turtle forward by a certain distance
my_turtle.forward(100)

# Rotate the turtle to the right by 90 degrees
my_turtle.right(90)

# Repeat the above steps to draw the remaining sides of the square
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)

# Close the turtle graphics window
turtle.done()"""
"""import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the initial color and width of the pen
my_turtle.pensize(3)
my_turtle.color("red")

# Move the turtle forward in a spiral pattern
for i in range(100):
    my_turtle.forward(i)
    my_turtle.right(91)
    my_turtle.color("green" if i % 2 == 0 else "blue")

# Close the turtle graphics window
turtle.done()"""
import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the initial color and width of the pen
my_turtle.pensize(3)
my_turtle.color("blue")

# Draw a circle
my_turtle.circle(100)

# Close the turtle graphics window
turtle.done()
