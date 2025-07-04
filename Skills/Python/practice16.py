class BinaryTree:
	def __init__(self, data): #constructor
		self.data = data
		self.right = None
		self.left = None

	def add_child_right(self, child):
		if self.right is None: # does node have right child?
			self.right = child
		else:
			print('Overwriting', self.right.data, 'by', child.data)
			self.right = child

	def add_child_left(self, child):
		if self.left is None: # does node have left child?
			self.left = child
		else:
			print('Overwriting', self.left.data, 'by', child.data)
			self.left = child
		

	def pretraverse(self):
		print(self.data) # 1 3 2 4 5
		if self.left is not None:
			self.left.pretraverse()
		
		if self.right is not None:
			self.right.pretraverse()

		return None #implicit



	def intraverse(self):
		if self.left is not None:
			self.left.intraverse()

		print(self.data) # 1 3 2 4 5
		
		if self.right is not None:
			self.right.intraverse()

		return None #implicit


	def posttraverse(self):
		
		if self.left is not None:
			self.left.posttraverse()

		if self.right is not None:
			self.right.posttraverse()


		print(self.data) # 1 3 2 4 5
		
		return None #implicit

	
		
#t =  BinaryTree('1')
#c1 =  BinaryTree('2')
#c2 =  BinaryTree('3')
#c3 =  BinaryTree('4')
#c4 =  BinaryTree('5')

#t.add_child_left(c2)
#t.add_child_right(c1) 
#c1.add_child_left(c3)
#c1.add_child_right(c4)

# 1
#3  2
# 4   5

t = BinaryTree('12')
c1 = BinaryTree('8')
c2 = BinaryTree('15')
c3 = BinaryTree('6')
c4 = BinaryTree('9')
c5 = BinaryTree('18')
c6 = BinaryTree('4')
c7 = BinaryTree('10')
c8 = BinaryTree('20')

t.add_child_left(c1)
t.add_child_right(c2)

c1.add_child_left(c3)
c1.add_child_right(c4)

c2.add_child_right(c5)

c3.add_child_left(c6)

c4.add_child_right(c7)

c5.add_child_right(c8)

print("Pre Order:\n")
t.pretraverse()
print("--------")
print("In Order:\n")
t.intraverse()
print("--------")
print("Post Order:\n")
t.posttraverse()