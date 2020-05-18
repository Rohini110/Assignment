import turtle
class Nanogon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(9):
            t.forward(self.side)
            t.right(40)
        turtle.done()
n = Nanogon()
n.set_side(100)
n.draw()
