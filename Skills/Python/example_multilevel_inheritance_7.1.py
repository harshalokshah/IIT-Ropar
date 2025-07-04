class Parent:
    
    def __init__(self, name):
        print('P', id(self))
        self.name = name

    def get_name(self):
        return self.name

class Child(Parent):

    def __init__(self, name, age):
        print('C', id(self))
        Parent.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age

class GrandChild(Child):

    def __init__(self, name, age, address):
        print('GC', id(self))
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address        

g = GrandChild("Nitin Auluck", 47, "IIT Ropar")
print(id(g))
print(g.get_name(), g.get_age(), g.get_address())
print(g)
print(g.name)
print(g.age)
print(g.address)

g.name = "NA"
print(g.get_name())
