import turtle
class Hexagon:
    def __init__(self, n = 0, l = 0):
        self.num = n
        self.length = l
    def set_props(self, n, l):
        self.num = n
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        angle = 360.0 / self.num

        for i in range(self.num):
            t.forward(self.length)
            t.right(angle)

        turtle.done()
h = Hexagon()
h.set_props(6, 70)
h.draw()