import turtle
class Rectangle:
    def __init__(self, l = 0, w = 0):
        self.__length = l
        self.__width = w
    def set_side(self, l, w):
        self.length = l
        self.width  = w
    def get_area(self):
        return (self.length * self.width)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.width)
        t.left(90)
r = Rectangle()
r.set_side(60, 30)
r.draw()