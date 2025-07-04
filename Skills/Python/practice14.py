# Node class
class Node:
        def __init__(self, data):
                self.data = data  # Assign data to new node
                self.next = None  # Initialize next as None, for new node

# Linked List class contains a Node object
class LinkedList:
        def __init__(self):
                self.head = None

        def traverse(self, node = None):
                if node is None: #head
                        node = self.head
                        
                print(node.data)
                if node.next is None: #tail
                        return 
                else:
                        self.traverse(node.next)


#       def insert(self, insert_node, after_node = None):
#               if after_node is None: #insert at the start
#                       insert_node.next = self.head
#                       self.head = insert_node
#                       return 
#               elif after_node.next is None: #insert at the end
#                       after_node.next = insert_node
#                       insert_node.next = None
#               else: #insert in the middle
#                       insert_node.next = after_node.next
#                       after_node.next = insert_node
                        

        def insert_beginning(self, insert_node):
                insert_node.next = self.head
                self.head = insert_node
                

        def insert_end(self, insert_node):
                last = self.head
                while (last.next):
                        last = last.next
                last.next = insert_node

        def insert_index(self, prev_node, new_node):
                new_node.next = prev_node.next
                prev_node.next = new_node

                        
        def delete(self, node_to_be_deleted):
                
                if self.head is None: #empty list
                        return

                start_node = self.head

                if start_node == node_to_be_deleted: #delete first node
                        self.head = node_to_be_deleted.next
                        return

                temp_node = self.head
                while temp_node.next is not None:
                        if temp_node.next == node_to_be_deleted: #delete middle node
                                temp_node.next = node_to_be_deleted.next
                                return

                        temp_node = temp_node.next

# Start with the empty list
llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
eleventh = Node(11)
sixth = Node(6)
#llist.head.next = second
#second.next = third
#third.next = fourth
#llist.traverse()

#llist.insert_beginning(second)
#llist.insert_beginning(third)
#llist.traverse()

llist.insert_end(second)
llist.insert_end(third)
llist.insert_end(fourth)
#llist.traverse()


llist.insert_index(fourth, eleventh)
llist.insert_index(fourth, sixth)
llist.traverse()

llist.delete(third)
llist.delete(eleventh)
llist.traverse()

#llist.insert(insert_node = fourth, after_node = second) #insert in the middle
#llist.traverse()

#llist.delete(fourth) #delete from middle
#llist.traverse()

#llist.insert(fourth) #insert at the start
#llist.traverse()

# llist.delete(fourth) #delete from the start
# llist.traverse()

#llist.insert(fourth, third) #insert at the end
#llist.traverse()

# llist.delete(fourth) #delete from the end
# llist.traverse()