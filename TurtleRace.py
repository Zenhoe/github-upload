import turtle
import random
import time

#Turtle Setup Class
class Turt():
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.Turt = turtle.Turtle()
        self.Turt.shape('turtle')
        self.Turt.color(color)
        self.Turt.penup()
        self.Turt.setposition(x, y)
        self.Turt.pensize(10)
        self.Turt.pendown()
        
    def Move(self):
        self.Turt.left(90)

    def WinnerLog(self):
        Ycord = self.Turt.ycor()
        WinnerLog = open("TurtWinnerData", "a")
        WinnerLog.write("    " + "\n")
        WinnerLog.write(self.color + " " + str(Ycord) + "\n")
        WinnerLog.close()

    def Boost(self):
        Cord = self.Turt.ycor()
        if Cord >= 302:
            self.Turt.speed(1)
        if  Cord < 300:
                self.Turt.forward(random.randint(5,60))

#Set up track
Painter = turtle.Turtle()
Painter.hideturtle()
Painter.color("white")
Painter.pencolor('black')
Painter.penup()
Painter.setpos(-400, 300)
Painter.pendown()
Painter.forward(800) 

Writer = turtle.Turtle()
Writer.hideturtle()
Writer.color("black")
Writer.penup()
Writer.setpos(0, 300)
Writer.pendown()
Writer.pensize(10)
Writer.write("Finish", font=("Robto", 50, "normal"), align="center")

#Turtle Racer set up          
T0 = Turt('red', 0, -300)
T1 = Turt('blue', 60, -300)
T2 = Turt('purple', 120, -300)
T3 = Turt('green', 180, -300)
T4 = Turt('pink', -60, -300)
T5 = Turt('orange', -120, -300)
T6 = Turt('black', -180, -300)
T0.Move()
T1.Move()
T2.Move()
T3.Move()
T4.Move()
T5.Move()
T6.Move()

#Tutle Race Movement
for turn in range(1,20):
    T0.Turt.forward(random.randint(1,60))
    T1.Turt.forward(random.randint(1,60))
    T2.Turt.forward(random.randint(1,60))
    T3.Turt.forward(random.randint(1,60))
    T4.Turt.forward(random.randint(1,60))
    T5.Turt.forward(random.randint(1,60))
    T6.Turt.forward(random.randint(1,60))
for X in range(1,4):  
    T0.Boost()
    T1.Boost()
    T2.Boost()
    T3.Boost()
    T4.Boost()
    T5.Boost()
    T6.Boost()

#Write Winner
if T0.Turt.ycor() > T1.Turt.ycor() and T0.Turt.ycor() > T2.Turt.ycor() and T0.Turt.ycor() > T3.Turt.ycor() and T0.Turt.ycor() > T4.Turt.ycor() and T0.Turt.ycor() > T5.Turt.ycor() and T0.Turt.ycor() > T6.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T0.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')
elif T1.Turt.ycor() > T0.Turt.ycor() and T1.Turt.ycor() > T2.Turt.ycor() and T1.Turt.ycor() > T3.Turt.ycor() and T1.Turt.ycor() > T4.Turt.ycor() and T1.Turt.ycor() > T5.Turt.ycor() and T1.Turt.ycor() > T6.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T1.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')
elif T2.Turt.ycor() > T0.Turt.ycor() and T2.Turt.ycor() > T1.Turt.ycor() and T2.Turt.ycor() > T3.Turt.ycor() and T2.Turt.ycor() > T4.Turt.ycor() and T2.Turt.ycor() > T5.Turt.ycor() and T2.Turt.ycor() > T6.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T2.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')
elif T3.Turt.ycor() > T1.Turt.ycor() and T3.Turt.ycor() > T2.Turt.ycor() and T3.Turt.ycor() > T0.Turt.ycor() and T3.Turt.ycor() > T4.Turt.ycor() and T3.Turt.ycor() > T5.Turt.ycor() and T3.Turt.ycor() > T6.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T3.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')
elif T4.Turt.ycor() > T0.Turt.ycor() and T4.Turt.ycor() > T2.Turt.ycor() and T4.Turt.ycor() > T3.Turt.ycor() and T4.Turt.ycor() > T0.Turt.ycor() and T5.Turt.ycor() and T6.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T4.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')
elif T5.Turt.ycor() > T0.Turt.ycor() and T5.Turt.ycor() > T1.Turt.ycor() and T5.Turt.ycor() > T3.Turt.ycor() and T5.Turt.ycor() > T4.Turt.ycor() and T5.Turt.ycor() > T0.Turt.ycor() and T5.Turt.ycor() > T6.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T5.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')
elif T6.Turt.ycor() > T0.Turt.ycor() and T6.Turt.ycor() > T1.Turt.ycor() and T6.Turt.ycor() > T3.Turt.ycor() and T6.Turt.ycor() > T2.Turt.ycor() and T6.Turt.ycor() > T4.Turt.ycor() and T6.Turt.ycor() > T0.Turt.ycor():
    Writer.penup()
    Writer.setpos(0,0)
    Writer.pendown()
    Writer.write(T6.color + " is the winner", font=('Roboto', 50, 'normal'), align='center')

WinnerLog = open("TurtWinnerData", "w")
WinnerLog.writelines("New Race!" + "\n")
WinnerLog.close()
T0.WinnerLog()
T1.WinnerLog()
T2.WinnerLog()
T3.WinnerLog()
T4.WinnerLog()
T5.WinnerLog()
T6.WinnerLog()

time.sleep(4)