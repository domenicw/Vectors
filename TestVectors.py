from Vector import Vector
from Point import Point
from Straight import Straight
from Plane import Plane

# basic math

print('Basic math')

print(Vector.__doc__)

first = Vector(1,1,1)
second = Vector(1,2,3)

first.print()
second.print()

print(first.norm())
print(second.norm())

third = first + second

print(third.norm())

print(first*second)

first.crossProduct(second).print()

(first - second).print()

print('\nDistances')

# distances

a = Point(1,5,3)
b = Point(2,3,4)
v = Vector(3,4,5)
s = Straight(b,None,v)
s.print()
print(s.distanceToPoint(a))
print(s.distanceToStraight(s))

v2 = Vector(1,1,1)
l = Plane(b,None,v,None,v2)
l.print()
print(l.distanceToPoint(a))
print(a.distanceToPlane(l))
print(a.distanceToPoint(b))
print(a.distanceToStraight(s))

print(l.distanceToPlane(l))
print(l.distanceToPoint(b))
print(b.distanceToStraight(s))

print('\nCenter')

# center

d = v.centerOfPolygon([a.toStationaryVector(),b.toStationaryVector()])
d.print()

d.toPoint().print()

print('\nAngle')

# angle

print(v.angleToVector(v2))
