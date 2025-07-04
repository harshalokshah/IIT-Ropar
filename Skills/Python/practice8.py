import math

class Point:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_


    def print_point(self):
        print(self.x, self.y, sep = ', ')


    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def midpoint(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx,my)



P1 = Point(4,3)
P1.print_point()

print('(%g, %g)' % (P1.x, P1.y))
distance = math.sqrt(P1.x**2 + P1.y**2)
print(distance)

P2 = Point(0,0)
P3 = Point(3,4)
P4 = Point(5,11)

P2 = Point.midpoint(P3, P4)
P2.print_point()

P2 = Point.add_point(P3, P4)
P2.print_point()

P2.x = 10
P2.y = 11
P2.print_point()

x = P2.x
print(x)

print(type(P2))
print(isinstance(P1, Point))
print(hasattr(P1, 'z'))