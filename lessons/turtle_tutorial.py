from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# Lines and Turning
leo.forward(50)  # move it forward to draw a line
leo.right(90)  # make the turtle move turn right by 90 degrees
leo.left(90)  # make the turtle move turn left by 90 degrees

# Goto, Penup and Pendown
# position our plot in a different spot on the screen
leo.penup()  # to prevent the turtle to draw
leo.goto(45, 60)  # to move the turlte to a new x, y position
leo.pendown()  # to allow the turtle to draw

# PenColor
colormode(255)
leo.color(99, 204, 250)  # (<red>, <green>, <blue>)

# Simplifying with loops
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()  
# to make sure the window does not close until this function done
# done() function must come after all of the turtle functions that I want to see on the window


# Fill Color
leo.begin_fill()  # to begin fill
# code for shape to filled
leo.end_fill()  # to end fill

# Other useful color commands
leo.pencolor("pink")  # to set only pen color
leo.fillcolor(32, 67, 93)  # to set only fill color
leo.color("green", "yellow")  # to set fill and pen color

# Speed, Visibility and the Fun Part
leo.speed(50)  # to change the speed
leo.hideturtle()  # to hide the cursor
