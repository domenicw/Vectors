import math

class Vector:
	'Vector in coordinate field'
	
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	
	def print(self):
		print('Vector ({0},{1},{2})'.format(self.a, self.b, self.c))
	
	def norm(self):
		return math.sqrt(self.a**2 + self.b**2 + self.c**2)
		
	def __add__(self,other):
		return Vector(self.a + other.a, self.b + other.b, self.c + other.c)
		
	def __mul__(self,other):
			return self.a*other.a + self.b*other.b + self.c*other.c
			
	def __sub__(self,other):
		return Vector(other.a-self.a, other.b-self.b, other.c-self.c)
	
	def toPoint(self):
		from Point import Point
		return Point(self.a, self.b, self.c)
	
	def crossProduct(self,other):
		a = self.b*other.c - self.c*other.b
		b = self.c*other.a - self.a*other.c
		c = self.a*other.b - self.b*other.a
		return Vector(a,b,c)
		
	def angleToVector(self,other):
		return math.degrees(math.acos((self * other) / (self.norm() * other.norm())))
		
		
	def centerOfPolygon(self,other):
		vector = self
		for vectors in other:
			vector += vectors
		factor = 1/(len(other)+1)
		return Vector(vector.a*factor, vector.b*factor, vector.c*factor)
