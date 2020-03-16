#PROJECT PTURTLE -- ROHAN FERNANDES -- TURTLE FUNCTIONS ONLY
#@NOTE: ONLY USE IF HAVE CONSENT FROM ROHAN FERNANDES 
#V 0.0.1 BETA PTURTLE -- MODIFY VERSION FOR PROJECT ATLAS: FAST, FUEL EFFICIENT, THE OFFICAL SPACE ROCKET OF THE FIREBOLT SPACE AGENCY (FSA)
from turtle import * #getting all functions from Turtle
import skyforce #import skyforce that is in shared folder

class VRTurtle:
    def __init__():
        hi = turtle.Pen()
    def goto(x,y):
        hi.penup()
        hi.goto(x,y)
        hi.pendown()
    def goto_line(x,y):
        hi.goto(x,y)
    def square(s):
        for i in range(4):
            hi.forward(s)
            hi.right(90)
    def rectangle(l,w):
        for i in range(2):
            hi.forward(l)
            hi.right(90)
            hi.forward(w)
            hi.right(90)
    def circle(r):
        hi.circle(r)
    def write(w):
        hi.write(w)
    def shape(sides,size):
        for i in range(sides):
            hi.forward(size)
            hi.right(360/sides)
    def part_circle(r,d):
        hi.circle(r,d)
    def left(degree):
        hi.left(degree)
    def right(degree):
        hi.right(degree)
    def diag(d):
        hi.setheading(d)
    def up(l):
        hi.forward(l)
    def r():
        left(90)
        up(10)
        part_circle(10,180)
        diag(45)
    def f():
        up(10)
        right(90)
        up(5)
        goto(0,0)
        up(5)
        right(90)
        up(5)
           ` goto(7,7)

    # @NOTE: This file is only for turtle functions, if wanted copy into directory and import into file to use for GUI Purpose, or use for using the function IN SEPERATE FILE. THIS FILE IS ONLY MEANT FOR 
    # @NOTE: TURTLE FUNCTION DEFINITIONS NOTHING ELSE

del hi