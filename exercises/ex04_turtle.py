"""Use turtle do draw a scene."""

__author__ = "730442764"

from turtle import Turtle, colormode, done

colormode(255)
 

def main() -> None:
    """The entrypoint of my scene."""
    star: Turtle = Turtle()
    house: Turtle = Turtle()
    treeleft: Turtle = Turtle()
    treeright: Turtle = Turtle()
    roof: Turtle = Turtle()
    sun: Turtle = Turtle()
    
    draw_house(house, 0, 0)
    draw_roof(roof, 0, 0)
    draw_treeleft(treeleft, -150, 0)
    draw_treeright(treeright, -150, 0)
    draw_star(star, -160, 0)
    
    import random
    x = random.randint(-300, 300)
    y = random.randint(130, 250)
    draw_sun(sun, x, y)

    done()


def draw_house(house: Turtle, x: float, y: float) -> None:
    """Draw a house whose top-left corner is located at x, y."""
    house.penup()
    house.goto(x, y)
    house.pendown()
    house.pensize(3)
    house.hideturtle()
    house.speed(50)
    house.pencolor(255, 126, 66)
    house.fillcolor(248, 220, 202)
    house.begin_fill()
    i: int = 0
    while i < 2:
        house.forward(300)
        house.right(90)
        house.forward(200)
        house.right(90)
        i = i + 1
    house.end_fill()


def draw_roof(roof: Turtle, x: float, y: float) -> None:
    """Draw a roof for the house."""
    roof.hideturtle()
    roof.pensize(3)
    roof.speed(50)
    roof.pencolor(255, 126, 66)
    roof.fillcolor(254, 179, 127)
    roof.begin_fill()
    roof.forward(300)
    roof.left(145)
    roof.forward(183)
    roof.left(70)
    roof.forward(183)
    roof.end_fill()


def draw_treeleft(treeleft: Turtle, x: float, y: float) -> None:
    """Draw the left side of the tree."""
    treeleft.penup()
    treeleft.goto(x, y)
    treeleft.pendown()
    treeleft.hideturtle()
    treeleft.pensize(3)
    treeleft.speed(50)
    treeleft.pencolor(27, 81, 26)
    treeleft.fillcolor(52, 149, 51)
    treeleft.setheading(225)
    treeleft.begin_fill()
    i: int = 3
    a: int = 40
    while i > 0:
        treeleft.forward(85)
        treeleft.right(225)
        treeleft.forward(a)
        treeleft.right(135)
        i = i - 1
        a = a + 20
    treeleft.end_fill()
    

def draw_treeright(treeright: Turtle, x: float, y: float) -> None:
    """Draw the right side of the tree."""
    treeright.penup()
    treeright.goto(x, y)
    treeright.pendown()
    treeright.hideturtle()
    treeright.pensize(3)
    treeright.speed(50)
    treeright.pencolor(27, 81, 26)
    treeright.fillcolor(52, 149, 51)
    treeright.setheading(315)
    treeright.begin_fill()
    i: int = 3
    a: int = 40
    while i > 0:
        treeright.forward(85)
        treeright.left(225)
        treeright.forward(a)
        treeright.left(135)
        i = i - 1
        a = a + 20
    treeright.end_fill()


def draw_star(star: Turtle, x: float, y: float) -> None:
    """Draw stars for the scene."""
    star.penup()  
    star.goto(x, y) 
    star.pendown()
    star.hideturtle()
    star.speed(50)
    star.pencolor(220, 220, 73)
    side_length: float = 20
    i: int = 0
    while (i < 70):
        star.forward(side_length)
        star.left(73.5)
        i = i + 1
        side_length = side_length * 0.98


def draw_sun(sun: Turtle, x: float, y: float) -> None:
    """Draw a sun and put it in random place of the scene."""
    sun.penup()
    sun.goto(x, y)
    sun.pendown()
    sun.speed(50)
    sun.hideturtle()
    sun.pencolor(252, 101, 0)
    sun.pensize(3)
    sun.fillcolor(245, 172, 47)
    sun.begin_fill()
    sun.circle(30)
    sun.end_fill()
    i: int = 0
    while i < 12:
        sun.right(90)
        sun.forward(20)
        sun.back(20)
        sun.left(90)
        i += 1
        sun.circle(30, 30)
        

if __name__ == "__main__":
    main()
