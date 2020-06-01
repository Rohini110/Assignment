# Shapes
import math
from abc import ABC, abstractmethod
#base abstract class
class Shape(ABC):
	@abstractmethod
	def printarea(self):
		pass
	@abstractmethod
	def printperimeter(self):
		pass
	@abstractmethod
	def get_sides(self):
		pass
		
		
class Rectangle(Shape):
	sides = 4
	
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
		
	def printarea(self):
		print("Area is:", self.length * self.breadth)
		
	def printperimeter(self):
		print("Perimeter is:", 2 * (self.length + self.breadth))
		
	def get_sides(self):
		print("Number of sides are:", self.sides)
		
#regPolygon is inherited from Shape
#Polymorphism is shown by printarea, printperimeter an get_sides function
class regPolygon(Shape):
	def __init__(self, nsides = 3, side = 4):
		self.n = nsides
		self.l = side
		
	def printarea(self, name):
		p = self.l * self.n
		a = p/math.tan(180/self.n)
		A = p * a
		print(f"Area of {name} is: ",A/2)
		
	def printperimeter(self, name):
		print(f"Perimeter of {name} is: ", self.n * self.l)
		
	def get_sides(self,name):
		print(f"Number of sides in a {name} are: ", self.n)
		
	
	
#Square is inherited from regPolygon
class Square(regPolygon):
	def diagonal(self):
		print("Length of diagonal is: ", math.sqrt(2) * self.l)
		
		

class Triangle(regPolygon):
	pass
	
class Rhombus(Shape):
	sides = 4
	def __init__(self, height, base):
		self.h = height
		self.b = base
		
	def printarea(self):
		print("Area of rhombus is: ", self.b * self.h)
		
	def printperimeter(self):
		print("Perimeter of rhombus is: ",self.b * 4)
		
	def get_sides(self):
		print("Number of sides in a rhombus are:", self.sides)
		
		
class Parallelogram(Rectangle):
	pass

class Trapezoid(Shape):
	sides = 4
	def __init__(self, height, base, s, c, d):
		self.h = height
		self.b = base
		self.s = s
		self.c = c
		self.d = d
		
	def printarea(self):
		print("Area of trapezoid is: ", (self.b + self.s) * self.h / 2)
		
	def printperimeter(self):
		print("Perimeter of trapezoid is: ",self.c + self.s + self.base + self.d)
		
	def get_sides(self):
		print("Number of sides in a trapezoid are:", self.sides)
	

class Circle:
	def __init__(self, r):
		self.radius = r
		
	def area(self):
		return math.pi * math.pow(self.radius,2)
		
	def circumference(self):
		return 2 * math.pi * (self.radius)
		 
class Ellipse(Circle):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def area(self):
		return math.pi * (self.a) * (self.b)
		
	def circumference(self):
		return math.pi * ((self.a) + self.b)
	
	
class Sphere(Circle):
	def surface_area(self):
		return 4 * super().area()
		
s = Sphere(4)
print(s.surface_area())
p = Parallelogram(3,4)
p.printarea()