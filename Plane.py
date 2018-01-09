
from Vector import Vector

class Plane:
	'Level in a coordinate field'
	
	def __init__(self,point,s,vectorS,t,vectorT):
		self.stationaryVectorToPoint = point.toStationaryVector()
		self.s = s
		self.vectorS = vectorS
		self.t = t
		self.vectorT = vectorT
		
	def print(self):
		t = self.t
		s = self.s
		
		if s is None:
			s = 's'
		if t is None:
			t = 't'
		
		print('({0},{1},{2}) + {3}*({4},{5},{6}) + {7}*({8},{9},{10})'.format(self.stationaryVectorToPoint.a, self.stationaryVectorToPoint.b, self.stationaryVectorToPoint.c, s, self.vectorS.a, self.vectorS.b, self.vectorS.c, t, self.vectorT.a, self.vectorT.b, self.vectorT.c))
		
	def distanceToPlane(self,other):
		vector = other.stationaryVectorToPoint - self.stationaryVectorToPoint
		crossProduct = self.vectorS.crossProduct(self.vectorT)
		distance = (vector * crossProduct) / crossProduct.norm()
		return abs(distance)
		
	def distanceToPoint(self,other):
		vector = other.toStationaryVector() - self.stationaryVectorToPoint
		crossProduct = self.vectorS.crossProduct(self.vectorT)
		distance = (vector * crossProduct) / crossProduct.norm()
		return abs(distance)
