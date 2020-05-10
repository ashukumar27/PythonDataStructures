## Binary Search Tree Implementaion

#Node class
class Node(object):
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


#Insert Operarion

class BinarySearchTree(object):

	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(data,self.root)

	#Complexity O(logn)
	def insertNode(self, data, node):
		if (data<node.data):
			if node.leftChild:
				self.insertNode(data,node.leftChild)
			else:
				node.leftChild = Node(data)
		else:
			if node.rightChild:
				self.insertNode(data, node.rightChild)
			else:
				node.rightChild = Node(data)

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)

	def removeNode(self, data, node):
		if not node:
			return node
		if data<node.data:
			node.leftChild = self.removeNode(data, node.leftChild)
		elif data>node.data:
			node.rightChild = self.removeNode(data, node.rightChild)
		else:#standing on the correct node
			if not node.leftChild and not node.rightChild:
				#it is a leaf node
				print("Removing a leaf node")
				del node
				return None # this is how a parent is informed that its l or r child is deleted, it is set to none

			if not node.leftChild:
				print("Removing the node with single right child")
				tempNode = node.rightChild
				del node;
				return tempNode
			elif not node.rightChild:
				print("Removing the node with singel left child")
				tempNode = node.leftChild
				del node
				return tempNode

			print("Removing node with two children")
			tempNode = self.getPredcessor(node.leftChild)
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data, node.leftChild)

		return node


	def getPredcessor(self, node):
		if node.rightChild:
			return self.getPredcessor(node.rightChild)

		return node

	def getMinValue(self):
		if self.root:
			return self.getMin(self.root)

	def getMin(self,node):
		if node.leftChild:
			return self.getMin(node.leftChild)

		return node.data

	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)

	def getMax(self, node):
		if node.rightChild:
			return self.getMax(node.rightChild)

		return node.data

	#InOrder Traversak
	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)

	def traverseInOrder(self, node):
		if node.leftChild:
			self.traverseInOrder(node.leftChild)

		print("%s "%node.data)

		if node.rightChild:
			self.traverseInOrder(node.rightChild)


bst = BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(1)
bst.remove(10)
#print(bst.getMinValue())

#rint(bst.getMaxValue())
bst.traverse()
#bst.insert()
