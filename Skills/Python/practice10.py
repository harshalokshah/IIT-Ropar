class Parent():
    def show(self):
        print("Inside Parent class")
class Child(Parent):
    def show(self):
        print("Inside Child class")
obj1 = Child()
obj1.show()
obj2 = Parent()
obj2.show()