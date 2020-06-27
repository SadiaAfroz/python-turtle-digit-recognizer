# use left mousepad to drag the object
# press right mousepad to clear the window(Redraw)
# press up button to complete drawing

from PIL import Image
from turtle import Screen, Turtle
import turtle
import epstopng


screen=Screen()
#screen.bgcolor("purple")
t=Turtle()
t.color('black','black')
t.speed(-1)
t.width(30)


def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)


def  changepos(x,y):
    t.penup()
    t.setpos((x,y))
    t.pendown()

def clickright(x,y):
    t.clear()
    
def captureScreen():
    ts=turtle.getscreen()
    ts.getcanvas().postscript(file='digit.eps')
    epstopng.converter()
    turtle.done()
    
    
def main(): 
    turtle.listen()
    t.ondrag(dragging)
    turtle.onscreenclick(clickright,3)
    turtle.onscreenclick(changepos,1)
    turtle.onkey(captureScreen, 'Up') 
    screen.mainloop()
    
main()


