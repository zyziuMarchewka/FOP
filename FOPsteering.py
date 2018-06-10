import sys
import tkinter as tk
import tk_tools
import turtle

t = turtle.Pen()

odc = 20
zajete = []


def ifin(trasa, lista):
    for i in range(len(lista)):
        if trasa[0] in lista[i] and trasa[1] in lista[i]:
            return 1
    return 0


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.button_grid = tk_tools.ButtonGrid(root, 3,
                                               ['Column0',
                                                'Column1',
                                                'Column2'])
        bg = self.button_grid

        bg.add_row([
                    ("nW", lambda: self.leftup()),
                    ("N", lambda: self.up()),
                    ("nE", lambda: self.rightup())
                  ])

        bg.add_row([
                    ("W", lambda: self.left()),
                    ("Menu", lambda: self.quit()),
                    ("E", lambda: self.right())
                  ])

        bg.add_row([
                    ("W", lambda: self.left()),
                    ("Menu", lambda: self.quit()),
                    ("E", lambda: self.right())
                  ])

    def quit(self):
        sys.exit()

    def up(self):
        x, y = t.pos()
        t.goto(x, y + odc)
        x2, y2 = t.pos()
        droga = ((x, y), (x2, y2))

        f = ifin(droga, zajete)
        if f:
            t.undo()

        zajete.append(droga)

    def down(self):
        x, y = t.pos()
        t.goto(x, y - odc)
        x2, y2 = t.pos()
        droga = ((x, y), (x2, y2))

        f = ifin(droga, zajete)
        if f:
            t.undo()

        zajete.append(droga)

    def right(self):
        x, y = t.pos()
        t.goto(x + odc, y)
        x2, y2 = t.pos()
        droga = ((x, y), (x2, y2))

        f = ifin(droga, zajete)
        if f:
            t.undo()

        zajete.append(droga)

    def left(self):
        x, y = t.pos()
        t.goto(x - odc, y)
        x2, y2 = t.pos()
        droga = ((x, y), (x2, y2))
        f = ifin(droga, zajete)
        if f:
            t.undo()

        zajete.append(droga)

    def leftup(self):
        pass

    def rightup(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
