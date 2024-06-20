import turtle

# Function to draw a rectangle
def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Set up the screen
screen = turtle.Screen()
screen.title("Draw a Rectangle with Turtle")
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.shape("circle")
t.color("white")
t.speed(1)  # Set the speed of the turtle (1 = slowest, 10 = fastest, 0 = no animation)

# Width and height of the rectangle
width = 400
height = 400

# Calculate the starting position
start_x = -width / 2
start_y = -height / 2

# Move the turtle to the starting position
t.penup()
t.goto(start_x, start_y)
t.pendown()

# Draw the rectangle
draw_rectangle(t, width, height)

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
