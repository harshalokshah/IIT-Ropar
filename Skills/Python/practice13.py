class Parent():
    def __init__(self):
        self.c = 21
        self._d = 42 # d is protected instance variable
    def get_d(self):
        return self._d
class Child(Parent):
    def __init__(self):
        self.e = 84
        Parent.__init__(self)
    def get_d(self):
        return self._d

object2 = Parent()
print(object2.get_d())

object1 = Child()
print(object1.get_d())