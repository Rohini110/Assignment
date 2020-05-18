import turtle
class Line:
    def __init__(self, l = 0):
        self.__length  = l
    def get_length(self):
        return  self.length
    def set_length(self, l):
        self.length = l
    def draw(self):
        t = turtle.Turtle()
        t.forward(self.length)
        turtle.done()
l = Line()
l.set_length(50)
l.draw()