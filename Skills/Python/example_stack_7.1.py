class Stack:
    def __init__(self): # stack constructor
        self.items = []

    def isEmpty(self): # is stack empty?
        return self.items == []

    def insert(self, item): #push
        self.items.append(item)

    def remove(self): #pop
        return self.items.pop()

    def size(self): #stack size
        return len(self.items)

    def peek(self): #return element at the head
        return self.items[len(self.items)-1]

    def print_stack(self): #print stack
        print(self.items)

     
s = Stack()
s.insert('a')
print(s.size())
s.insert('b')
print(s.size())
print(s.peek())
s.insert('c')
s.insert('d')
print(s.size())
#print(s.peek())
print(s.remove())
s.print_stack()


