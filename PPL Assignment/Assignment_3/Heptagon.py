import turtle
class Heptagon:
    def __init__(self, s = 0):
        self.__side = s
    def set_side(self, s):
        self.side = s
    def get_side(self):
        return self.side
    def draw(self):
        t = turtle.Turtle()
        for i in range(7):
            t.forward(self.side)
            t.right(51.42)
        turtle.done()
h = Heptagon()
h.set_side(100)
h.draw()
