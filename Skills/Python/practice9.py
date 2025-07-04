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


class Rectangle (Point):
     

    def __init__(self, w, h, x, y):
        self.width = w
        self.height = h
        self.corner = Point(x,y)
       
    def find_center(rect):  
        p = Point(0,0)
        p.x = rect.corner.x + rect.width/2.0
        p.y = rect.corner.y + rect.height/2.0
        return p


    def grow_rectangle(rect, dwidth, dheight):
        rect.width += dwidth
        rect.height += dheight



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

print("####")

box = Rectangle(100, 200, 0, 0)

print(box.height)
print(box.width)
print(box.corner.x, box.corner.y, sep = ', ')

center = box.find_center()
center.print_point()

box.grow_rectangle(50, 100)
print(box.width)
print(box.height)
