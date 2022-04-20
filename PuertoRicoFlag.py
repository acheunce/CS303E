# File: PuertoRicoFlag.py
# Student: Aaron Cheung 
# UT EID: ac77373
# Course Name: CS303E
# 
# Date: 04/20/2022
# Description of Program: Graphic of the Puerto Rico Flag

import turtle

def drawRectangle(ttl, width, height):
    ttl.forward(width)
    ttl.left(90)
    ttl.forward(height)
    ttl.left(90)
    ttl.forward(width)
    ttl.left(90)
    ttl.forward(height)

def fillRectangle(ttl, width, height, fill, color):
    if fill:
        ttl.fillcolor(color)
        ttl.begin_fill()
        drawRectangle(ttl, width, height)
        ttl.end_fill()
    else:
        drawRectangle(ttl, width, height)

def drawTriangle(ttl, v1, v2, v3):
    ttl.pendown()
    ttl.goto(v2)
    ttl.goto(v3)
    ttl.goto(v1)

def fillTriangle(ttl, v1, v2, v3, fill, color):
    if fill:
        ttl.fillcolor(color)
        ttl.begin_fill()
        drawTriangle(ttl, v1, v2, v3)
        ttl.end_fill()
    else:
        drawTriangle(ttl, v1, v2, v3)

def drawPuertoRicoFlag(ttl, x, y):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0) # point east
    ttl.pendown()
    drawRectangle(ttl, 600, 400)
    
    ttl.setheading(0)
    fillRectangle(ttl, 600, 80, True, 'firebrick1')

    ttl.setheading(0)
    ttl.penup()
    ttl.goto(x, y + 160)
    ttl.pendown()
    fillRectangle(ttl, 600, 80, True, 'firebrick1')

    ttl.setheading(0)
    ttl.penup()
    ttl.goto(x, y + 320)
    ttl.pendown()
    fillRectangle(ttl, 600, 80, True, 'firebrick1')

    ttl.penup()
    ttl.goto(x, y)

    fillTriangle(ttl, (-300, -200), (0,0), (-300, 200), True, 'navy')

    





# red (255,0 0)
# blue (0, 0, 225)

flag = turtle.Turtle()
flag.speed(10)
drawPuertoRicoFlag(flag, -300, -200)

turtle.done()