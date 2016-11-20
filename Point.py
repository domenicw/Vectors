from Vector import Vector

class Point:
	'Point in coordinate field'
	
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
		
	def print(self):
		print('Point at ({0},{1},{2})'.format(self.a, self.b, self.c))
		
	def toStationaryVector(self):
		return Vector(self.a, self.b, self.c)
		
	def distanceToPoint(self,other):
		return (Vector(self.a, self.b, self.c) - Vector(other.a, other.b, other.c)).norm()
		
	def distanceToLevel(self,other):
		vector = self.toStationaryVector() - other.stationaryVectorToPoint
		crossProduct = other.vectorS.crossProduct(other.vectorT)
		distance = (vector * crossProduct) / crossProduct.norm()
		return abs(distance)
		
	def distanceToStraight(self,other):
		vector = self.toStationaryVector() - other.stationaryVectorToPoint
		distance = vector.crossProduct(other.vector).norm() / other.vector.norm()
		return abs(distance)
