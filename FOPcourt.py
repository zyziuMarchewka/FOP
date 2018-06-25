from FOPmain import *

px2 = 0
py2 = 0

def Classic(xsize, ysize):
    def forw():
        global px2
        global py2
        px, py = t.position()
        zajete.append(((px, py),(px2, py2)))
        t.fd(odc)
        px2 = px
        py2 = py
    t.speed(0)
    t.pencolor("lightblue")

    t.up()
    t.goto(-400, 400)
    t.down()
    t.seth(270)
    for i in range(800//odc):
        t.fd(800)
        t.back(800)
        x, y = t.position()
        t.goto(x+odc, y)
    t.up()
    t.goto(-400, 400)
    t.down()
    t.seth(0)
    for i in range(800//odc):
        t.fd(800)
        t.back(800)
        x, y = t.position()
        t.goto(x, y-odc)

    t.seth(90)
    t.up()
    t.goto(0-(xsize/2+1)*odc, 0)
    t.down()
    t.pencolor("black")
    t.speed(0)
    for i in range(2):
        px2, py2 = t.position()
        t.fd(odc)
        t.right(90)
        forw()
        t.left(90)
        for j in range((ysize//2)-1):
            forw()
        t.right(90)
        for j in range(xsize):
            forw()
        t.right(90)
        for j in range((ysize//2)-1):
            forw()
        t.left(90)
        forw()
        t.right(90)
        forw()

Classic(20, 10)
t.up()
t.goto(0, 0)
t.down()
t.color("black", "black")
t.shape("circle")
t.turtlesize(0.25)