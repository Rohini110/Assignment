import turtle
class Triangle:
    def __init__(self, s1 = 0, s2 = 0, s3 = 0):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    def set_side(self, s1, s2, s3):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
    def get_side(self):
        return (self.side1, self.side2, self.side3)
    def get_perimeter(self):
        return (self.side1 + self.side2 + self.side3)
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.side1)
        t.left(120)
        t.forward(self.side2)
        t.left(120)
        t.forward(self.side3)
       # t.left(120)
        turtle.done()
t = Triangle()
t.set_side(30, 30, 30)
t.draw()