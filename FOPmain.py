import turtle as t
import sys
import tkinter as tk
import tk_tools

odc = 10


zajete = []
border = []
Player = 1
turn = 1
move = 1


from FOPcourt import *
from FOPsteering import *

Classic(50, 20)
t.up()
t.goto(0, 0)
t.down()
t.color("blue", "blue")
t.seth(0)
t.turtlesize(0.75)