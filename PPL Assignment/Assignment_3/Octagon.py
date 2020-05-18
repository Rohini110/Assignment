import turtle
class Octagon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(8):
            t.forward(self.side)
            t.right(45)
        turtle.done()
o = Octagon()
o.set_side(100)
o.draw()
