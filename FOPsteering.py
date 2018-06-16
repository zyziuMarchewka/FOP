from time import sleep
import sys
import tkinter as tk
import tk_tools
import turtle
from decimal import Decimal

t = turtle.Pen()

odc = 20
zajete = []


def ifRoutein(trasa, lista):
    for i in range(len(lista)):
        if trasa[0] in lista[i] and trasa[1] in lista[i]:
            return 1
    return 0

def ifin(point, lista):
    for i in range(len(lista)-1):
        if point in lista[i]:
            return(1)
    return 0


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets(1)
    def create_widgets(self, player):
        self.button_grid = tk_tools.ButtonGrid(root, 3,
                                               [' - - -', f' P {player}', '- - - '])
        bg = self.button_grid

        bg.add_row([
            ("nW", lambda: self.move(-1, 1)),
            ("N", lambda: self. move(0, 1)),
            ("nE", lambda: self.move(1, 1))
        ])

        bg.add_row([
            ("W", lambda: self.move(-1, 0)),
            ("Exit", lambda: self.quit()),
            ("E", lambda: self.move(1, 0))
        ])

        bg.add_row([
            ("sW", lambda: self.move(-1, -1)),
            ("S", lambda: self.move(0, -1)),
            ("sE", lambda: self.move(1, -1))
        ])

    def menu(self):
        print('Opcja "Menu" jeszcze nie gotowa.')
        # TODO: menu - opcje takie jak "exit", "restart" itp.

    def quit(self):
        sys.exit()

    def clear(self):
        list = root.grid_slaves()
        for l in list:
            l.destroy()

    def move(self, x, y):
        px, py = t.pos()
        t.goto(px+ (x*odc), py + (y*odc))
        px2, py2 = t.pos()
        droga = ((px, py), (px2, py2))

        f = ifRoutein(droga, zajete)
        if f:
            t.undo()

        zajete.append(droga)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()



tk.mainloop()