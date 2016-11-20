from Vector import Vector

class Straight:
	'Straight in coordinate Field'
	
	def __init__(self,point,t,vector):
		self.t = t
		self.stationaryVectorToPoint = point.toStationaryVector()
		self.vector = vector
		
	def print(self):
		t = self.t
		
		if t is None:
			t = 't'
		
		print('({0},{1},{2}) + {3}*({4},{5},{6})'.format(self.stationaryVectorToPoint.a, self.stationaryVectorToPoint.b, self.stationaryVectorToPoint.c, t, self.vector.a, self.vector.b, self.vector.c))
		
	def distanceToStraight(self,other):
		if ((self.stationaryVectorToPoint.a % other.stationaryVectorToPoint.a == 0) and (self.stationaryVectorToPoint.b % other.stationaryVectorToPoint.b == 0) and (self.stationaryVectorToPoint.c % other.stationaryVectorToPoint.c == 0)):
			vector = other.stationaryVectorToPoint - self.stationaryVectorToPoint
			distance = (vector * self.vector) / self.vector.norm()
			return abs(distance)
			
		else:
			vector = other.stationaryVectorToPoint - self.stationaryVectorToPoint
			crossProduct = self.vector.crossProduct(other.vector)
			distance = (vector * crossProduct) / crossProduct.norm()
			return abs(distance)
			
	def distanceToPoint(self,other):
		vector = other.toStationaryVector() - self.stationaryVectorToPoint
		distance = vector.crossProduct(self.vector).norm() / self.vector.norm()
		return distance
