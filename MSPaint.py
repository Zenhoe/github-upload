import turtle
from turtle import Turtle, Screen
screen = Screen()
DrawingTurt = turtle.Turtle()
DrawingTurt.color('black')
DrawingTurt.speed(-1)
DrawingTurt.shape('circle')
DrawingTurt.shapesize(.5)


def Dragging(x,y):
    DrawingTurt.ondrag(None)
    DrawingTurt.setheading(DrawingTurt.towards(x,y))
    DrawingTurt.goto(x,y)
    DrawingTurt.ondrag(Dragging)

def ClearClick(x,y):
    DrawingTurt.clear()

def SizePress1():
    DrawingTurt.pensize(10)
    DrawingTurt.shapesize(.5)

def SizePress2():
    DrawingTurt.pensize(20)
    DrawingTurt.shapesize(1)

def SizePress3():
    DrawingTurt.pensize(30)
    DrawingTurt.shapesize(2)

def SizePress4():
    DrawingTurt.pensize(40)
    DrawingTurt.shapesize(3)
    
def ColorChangeR():
    DrawingTurt.pencolor('red')

def ColorChangeB():
    DrawingTurt.pencolor('blue')

def ColorChangeO():
    DrawingTurt.pencolor('orange')

def ColorChangeY():
    DrawingTurt.pencolor('yellow')

def ColorChangeP():
    DrawingTurt.pencolor('purple')

def ColorChangeG():
    DrawingTurt.pencolor('green')

def ColorChangeBl():
    DrawingTurt.color('red')
    DrawingTurt.pencolor('black')

def Earse():
    DrawingTurt.color('black')
    DrawingTurt.pencolor('white')
    DrawingTurt.pensize(15)
    DrawingTurt.shapesize(.5)
def Main():
    turtle.listen()
    DrawingTurt.ondrag(Dragging)
    turtle.onscreenclick(ClearClick, 3)
    turtle.onkeypress(SizePress1, '1')
    turtle.onkeypress(SizePress2, '2')
    turtle.onkeypress(SizePress3, '3')
    turtle.onkeypress(SizePress4, '4')
    turtle.onkeypress(ColorChangeR, 'q')
    turtle.onkeypress(ColorChangeB, 'w')
    turtle.onkeypress(ColorChangeO, 'e')
    turtle.onkeypress(ColorChangeY, 'r')
    turtle.onkeypress(ColorChangeP, 't')
    turtle.onkeypress(ColorChangeG, 'y')
    turtle.onkeypress(ColorChangeBl, 'u')
    turtle.onkeypress(Earse, 'i')
    screen.mainloop()

Main()