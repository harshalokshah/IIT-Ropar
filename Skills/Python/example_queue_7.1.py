class Queue:
    def __init__(self): # queue constructor
        self.items = []

    def isEmpty(self): # is queue empty?
        return self.items == []

    def insert(self, item): #enqueue
        self.items.insert(0,item)

    def remove(self): #dequeue
        return self.items.pop()

    def size(self): #queue size
        return len(self.items)

    def peek(self): #return element at the queue head
        return self.items[len(self.items)-1]

    def print_queue(self): #print queue
        print(self.items)

    
q = Queue()
q.insert('a')
#print(q.size())
q.insert('b')
#print(q.size())
print(q.peek())
q.insert('c')
q.insert('d')
q.insert('e')
q.remove()
print(q.peek())
q.print_queue()
