from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

colormode(255)
leo.pencolor(184, 4, 11)
leo.fillcolor(247, 178, 203)

leo.penup()  
leo.goto(20, 40) 
leo.pendown()
leo.speed(30)
leo.pensize(3)  # we want to make the border wider

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob.penup()  
bob.goto(20, 40) 
bob.pendown()
bob.speed(50)
bob.pencolor("black")

side_length: float = 300

while (i < 150):
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
    side_length = side_length * 0.98
done()
