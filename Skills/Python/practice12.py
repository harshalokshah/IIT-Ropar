class Parent():
    def __init__(self):
        self.c = 21
        self.d = 42
    def set_d(self, d):
        if d > 0:
            self.d = d
        else:
            self.d = 0
    def get_d(self):
        return self.d

object1 = Parent()
object1.d = 43 #should produce an error, but doesn't
print(object1.get_d())
object1.set_d(43)
print(object1.get_d())