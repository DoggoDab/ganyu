import turtle as t
from turtle import Turtle

# move the cursor to the left to draw left eye
def left_eye():
    t.penup()
    t.setx(-300)
    t.sety(-160)
    t.rt(80)
    t.pendown()

    # draw left eye
    for _ in range(360): 
        t.lt(0.3)
        t.fd(0.57)

    t.penup()
    t.goto(-300, -160)
    t.pendown()

    t.lt(15)
    for _ in range(320): 
        t.lt(-0.2)
        t.fd(0.56)

    t.penup()
    t.goto(-140, -235)
    t.left(90)
    t.pendown()

    for _ in range(180): 
        t.lt(0.2)
        t.fd(0.6)

    t.penup()
    t.goto(-160, -155)
    t.lt(15)
    t.pendown()

    bLE = 4
    t.tracer(False)
    for i in range(120): 
        if 0 <= i < 30 or 60 <= i < 90: 
            bLE -= 0.05
            t.lt(3)
            t.fd(bLE)

        else: 
            bLE += 0.05
            t.lt(3)
            t.fd(bLE)
    t.tracer(True)


def right_eye(): 
    t.penup()
    t.goto(200, -170)
    t.lt(135)
    t.pendown()

    for _ in range(360): 
        t.rt(0.3)
        t.fd(0.57)

    t.penup()
    t.goto(200, -170)
    t.pendown()

    t.rt(15)
    for _ in range(320): 
        t.rt(-0.2)
        t.fd(0.56)

    t.penup()
    t.goto(40, -237)
    t.rt(90)
    t.pendown()

    for _ in range(180): 
        t.rt(0.2)
        t.fd(0.65)

    t.penup()
    t.goto(60, -150)
    t.rt(15)
    t.pendown()

    bRE = 4
    t.tracer(False)
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            bRE -= 0.05
            t.rt(3)
            t.fd(bRE)

        else:
            bRE += 0.05
            t.rt(3)
            t.fd(bRE)
    t.tracer(True)

def left_pupil(): 
    t.penup()
    t.goto(115, -190)
    t.lt(35)
    t.pendown()

    cLP = 1.5
    t.tracer(False)
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90: 
            cLP -= 0.05
            t.lt(3)
            t.fd(cLP)

        else:
            cLP += 0.05
            t.lt(3)
            t.fd(cLP)
    t.tracer(True)

def right_pupil(): 
    t.penup()
    t.goto(-200, -190)
    t.rt(3)
    t.pendown()

    cRP = 1.5
    t.tracer(False)
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90: 
            cRP -= 0.05
            t.lt(3)
            t.fd(cRP)

        else: 
            cRP += 0.05
            t.lt(3)
            t.fd(cRP)
    t.tracer(True)

#eyelashes
def left_eyelashes(): 
    t.penup()
    t.goto(-280, -210)
    t.lt(80)
    t.pendown()

    for _ in range(60):
        t.rt(1.3)
        t.fd(1.7)

    t.rt(60)

    for _ in range(20):
        t.rt(0.3)
        t.fd(1)

    t.lt(140)
    t.fd(30)
    t.rt(160)
    t.fd(40)

    for _ in range(50): 
        t.lt(0.6)
        t.fd(1)

    t.lt(90)
    t.fd(40)
    t.lt(200)
    t.fd(50)
    t.lt(60)

    for _ in range(50):
        t.rt(0.3)
        t.fd(1)

    t.lt(90)
    t.fd(40)
    t.lt(200)
    t.fd(50)
    t.lt(60)

    for _ in range(125):
        t.rt(0.5)
        t.fd(0.5)

    t.lt(40)
    t.bk(20)

    for _ in range(70): 
        t.rt(0.5)
        t.fd(0.5)

    t.lt(40)
    t.bk(40)

def right_eyelashes(): 
    t.penup()
    t.goto(170, -220)
    t.lt(25)
    t.pendown()

    for _ in range(68): 
        t.lt(1.3)
        t.fd(1.7)

    t.lt(60)

    for _ in range(20): 
        t.rt(0.3)
        t.fd(1)

    t.rt(140)
    t.fd(30)
    t.lt(160)
    t.fd(40)

    for _ in range(45): 
        t.rt(0.6)
        t.fd(1)

    t.rt(90)
    t.fd(40)
    t.rt(200)
    t.fd(50)
    t.rt(60)

    for _ in range(50): 
        t.lt(0.3)
        t.fd(1)

    t.rt(90)
    t.fd(40)
    t.rt(200)
    t.fd(50)
    t.rt(60)

    for _ in range(135): 
        t.lt(0.5)
        t.fd(0.6)

    t.rt(40)
    t.bk(20)

    for _ in range(70): 
        t.lt(0.5)
        t.fd(0.5)

    t.rt(45)
    t.bk(40)

def hair(): 
    t.penup()
    t.goto(90, 130)
    t.lt(75)
    t.pendown()

    for _ in range(700): 
        t.rt(0.1)
        t.fd(0.5)

    t.lt(30)

    for _ in range(710): 
        t.lt(0.1)
        t.bk(0.4)

    t.penup()
    t.goto(-60, -60)
    t.lt(30)
    t.pendown()

    for _ in range(600):
        t.rt(0.1)
        t.bk(0.5)

    t.rt(30)
    for _ in range(300): 
        t.lt(0.2)
        t.fd(0.7)

    t.lt(30)

    for _ in range(300): 
        t.rt(0.09)
        t.bk(0.5)

    t.rt(10)

    for _ in range(300): 
        t.lt(0.09)
        t.fd(0.3)

    t.lt(20)

    for _ in range(200): 
        t.rt(0.3)
        t.bk(0.8)

    t.penup()
    t.goto(-300, 40)
    t.rt(20)
    t.pendown()

    for _ in range(400): 
        t.rt(0.1)
        t.fd(0.4)

    t.lt(40)

    for _ in range(500): 
        t.lt(0.1)
        t.fd(0.5)

    t.rt(20)
    t.penup()
    t.goto(-410, -360)
    t.pendown()

    t.rt(20)

    for _ in range(300): 
        t.lt(0.095)
        t.bk(0.5)

    t.penup()
    t.goto(-380, -100)
    t.pendown()

    t.bk(50)
    t.rt(20)

    for _ in range(200): 
        t.rt(0.1)
        t.bk(0.5)

    t.penup()
    t.goto(90, 123)
    t.pendown()

    t.lt(35)

    for _ in range(520): 
        t.lt(0.1)
        t.fd(0.5)

    t.rt(90)

    for _ in range(200): 
        t.lt(0.15)
        t.bk(1)

    t.penup()
    for _ in range(200): 
        t.rt(0.15)
        t.fd(1)
    t.pendown()

    t.lt(30)

    for _ in range(600): 
        t.rt(0.1)
        t.fd(0.6)

    t.penup()
    for _ in range(300): 
        t.lt(0.1)
        t.bk(0.6)
    t.pendown()

    t.rt(30)
    for _ in range(450): 
        t.lt(0.1)
        t.bk(0.6)

    t.penup()
    t.goto(-490, -360)
    t.pendown()

    t.rt(10)
    t.bk(160)

    for _ in range(250):
        t.lt(0.1)
        t.bk(0.8)

    t.rt(40)
    t.bk(25)

    t.penup()
    t.lt(40)
    t.fd(25)
    for _ in range(125): 
        t.rt(0.1)
        t.fd(0.8)
    t.rt(90)
    t.fd(15)
    t.pendown()

    t.rt(40)
    t.fd(25)

    t.penup()
    t.goto(-470, -280)
    t.pendown()

    for _ in range(150): 
        t.rt(0.2)
        t.fd(0.8)

    t.rt(20)

    for _ in range(150): 
        t.rt(0.1)
        t.fd(1)

    t.lt(1)
    for _ in range(150): 
        t.rt(0.2)
        t.fd(1.5)

    t.rt(5)
    t.fd(130)

    t.rt(30)
    t.fd(200)

    t.rt(40)
    t.fd(20)

    t.lt(80)
    t.fd(20)

    t.rt(60)
    t.fd(30)

    t.lt(30)
    t.fd(30)

    t.rt(60)
    t.fd(50)

    t.lt(40)
    t.fd(60)

    t.rt(40)
    t.fd(80)

    t.penup()
    t.goto(-15, 290)
    t.lt(40)
    t.pendown()

    t.fd(150)

    t.rt(30)
    t.fd(150)

    t.rt(20)
    t.fd(200)

    for _ in range(75): 
        t.rt(0.5)
        t.fd(1.5)

    t.penup()
    t.lt(185)
    t.goto(400, -360)
    t.pendown()

    t.fd(100)
    t.rt(40)
    for _ in range(270): 
        t.lt(0.1)
        t.fd(1)

    t.penup()
    t.goto(430, -360)
    t.pendown()

    t.lt(20)
    t.fd(125)

    t.penup()
    t.goto(-570, -360)
    t.pendown()

    t.rt(30)
    t.fd(170)

    t.penup()
    t.goto(-520, -360)
    t.lt(40)
    t.pendown()

    for _ in range(100): 
        t.rt(0.4)
        t.fd(0.7)

    t.penup()
    t.goto(-200, 190)
    t.rt(110)
    t.pendown()

    for _ in range(250): 
        t.lt(0.1)
        t.fd(0.8)

    t.rt(20)
    for _ in range(100): 
        t.rt(0.3)
        t.bk(0.8)

    t.lt(30)
    for _ in range(100): 
        t.rt(0.1)
        t.fd(0.6)

    t.penup()
    t.goto(93, 130)
    t.lt(55)
    t.pendown()

    t.fd(40)
    t.rt(30)

    for _ in range(300): 
        t.rt(0.1)
        t.bk(0.6)

    t.penup()
    t.goto(-105, 310)
    t.lt(110)
    t.pendown()

    for _ in range(200):
        t.rt(0.7)
        t.fd(1.5)

    t.penup()
    t.goto(-60, 312)
    t.pendown()

    t.rt(15)
    for _ in range(40):
        t.rt(0.3)
        t.bk(0.5)

    t.penup()
    t.goto(-530, -40)
    t.rt(40)
    t.pendown()

    for _ in range(200): 
        t.rt(0.1)
        t.fd(0.7)

    t.rt(80)
    t.bk(60)

    t.lt(70)
    t.bk(80)

    t.penup()
    t.goto(455, -10)
    t.lt(100)
    t.pendown()

    for _ in range(100):
        t.lt(0.2)
        t.fd(0.8)

    t.lt(30)
    t.bk(35)

    t.rt(10)

    for _ in range(200): 
        t.lt(0.1)
        t.fd(0.5)

    t.lt(65)
    t.bk(60)

    t.rt(65)
    t.bk(85)

def right_horn(): 
    t.penup()
    t.goto(320, 185)
    t.pendown()

    t.rt(5)
    t.fd(125)

    t.rt(35)
    t.fd(75)

    t.rt(25)
    t.fd(75)

    t.rt(20)
    for _ in range(115): 
        t.lt(0.08)
        t.fd(1)

    t.penup()
    t.fd(60)
    t.pendown()

    for _ in range(160):
        t.lt(0.6)
        t.fd(1)

    t.lt(20)
    for _ in range(240): 
        t.rt(0.3)
        t.bk(1)

def left_horn(): 
    t.penup()
    t.goto(-410, 180)
    t.rt(130)
    t.pendown()

    t.fd(125)

    t.lt(35)
    t.fd(75)

    t.lt(30)
    t.fd(75)

    t.lt(25)
    for _ in range(120): 
        t.rt(0.08)
        t.fd(1)

    t.penup()
    t.fd(80)
    t.pendown()

    for _ in range(165):
        t.rt(0.6)
        t.fd(1)

    t.rt(20)
    for _ in range(160): 
        t.lt(0.3)
        t.bk(1)

def ganyu(): 
    left_eye()
    right_eye()
    left_pupil()
    right_pupil()
    left_eyelashes()
    right_eyelashes()
    hair()
    right_horn()
    left_horn()

if __name__ == '__main__': 
    a = Turtle()
    t.screensize(800, 800)
    t.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    ganyu()
    t.hideturtle()
    a.screen.mainloop()