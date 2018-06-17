from time import sleep
import sys
import tkinter as tk
import tk_tools
import turtle
from decimal import Decimal

t = turtle.Pen()

odc = 20
zajete = []
Player = 1


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
        self.create_widgets(2)

    def create_widgets(self, player):
        self.button_grid = tk_tools.ButtonGrid(root, 3,
                                               [' - - -', f' P {player}', '- - - '])
        bg = self.button_grid

        bg.add_row([
            ("nW", lambda: self.move(-1, 1, player)),
            ("N", lambda: self. move(0, 1, player)),
            ("nE", lambda: self.move(1, 1, player))
        ])

        bg.add_row([
            ("W", lambda: self.move(-1, 0, player)),
            ("Exit", lambda: self.quit()),
            ("E", lambda: self.move(1, 0, player))
        ])

        bg.add_row([
            ("sW", lambda: self.move(-1, -1, player)),
            ("S", lambda: self.move(0, -1, player)),
            ("sE", lambda: self.move(1, -1, player))
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

    def move(self, x, y, player2):
        global Player
        if player2 != Player:
            return
        px, py = t.pos()
        t.goto(px+ (x*odc), py + (y*odc))
        px2, py2 = t.pos()
        droga = ((px, py), (px2, py2))

        f = ifRoutein(droga, zajete)
        if f:
            t.undo()

        zajete.append(droga)
        f = ifin((px2, py2), zajete)
        if f != 1:
            Player = 3-Player
            print(f'Turn of Player {Player}')



if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()