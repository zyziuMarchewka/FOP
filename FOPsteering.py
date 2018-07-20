from FOPmain import *


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
                                               [f'T {turn}', f' P {player}', f'M {move}'])
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
            ("sW", lambda: self.move(-1, -1,)),
            ("S", lambda: self.move(0, -1)),
            ("sE", lambda: self.move(1, -1))
        ])

    def start(self):
        global Player
        self.clear()
        self.create_widgets(Player)

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
        # TODO: win check, "out"
        global Player
        global move
        global turn

        px, py = t.pos()
        t.goto(px+ (x*odc), py + (y*odc))
        px2, py2 = t.pos()
        droga = ((px, py), (px2, py2))

        f = ifRoutein(droga, zajete)

        if f:
            t.undo()
            move -= 1
        zajete.append(droga)
        move += 1

        f = ifin((px2, py2), zajete)
        if f != 1:
            Player = 3-Player
            self.clear()
            self.bg = tk_tools.ButtonGrid(root, 1, [f"next turn of player {Player}"])
            self.bg.add_row([("start", lambda: self.start())])
            if Player == 1:
                t.color("blue", "blue")
                t.seth(0)
            else:
                t.color("green", "green")
                t.seth(180)
            turn += 1
            move = 1
        else:
            self.clear()
            self.create_widgets(Player)


if __name__ == '__main__':
    t.speed(1)
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
