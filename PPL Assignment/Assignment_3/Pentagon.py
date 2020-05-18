import turtle
class Pentagon:
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
p = Pentagon()
p.set_props(5, 70)
p.draw()