class Node(object):
	def __init__(self, data):
		self.data = data;
		self.nextNode = None;

class LinkedList(object):
	def __init__(self):
		self.head = None;
		self.size=0; # so theat we can calculate size in O(1)

	#O(1)	
	def insertStart(self, data):
		self.size= self.size+1;
		newNode = Node(data)

		if not self.head:
			self.head = newNode;
		else:
			newNode.nextNode = self.head;
			self.head = newNode;

	#O(1) for calculating size
	def size1(self):
		return self.size;

	#O(n) for calculating size
	def size2(self):
		actualNode = self.Node;
		size=0;
		while actualNode is not None:
			size+= 1;
			actualNode = actualNode.nextNode;

	def remove(self, data):
		if self.head is None:
			return;

		self.size = self.size-1;

		currentNode = self.head;
		previousNode=None;

		while currentNode.data != data:
			previousNode = currentNode;
			currentNode = currentNode.nextNode;

		if previousNode is None:
			self.head = currentNode.nextNode;
		else:
			previousNode.nextNode = currentNode.nextNode;


	#O(n)
	def insertEnd(self,data):
		self.size = self.size+1;
		newNode = Node(data);
		actualNode = self.head;

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode;

		actualNode.nextNode = newNode

	def traverseList(self):
		actualNode = self.head;

		while actualNode is not None:
			print("%d" %actualNode.data)
			actualNode = actualNode.nextNode;



ll = LinkedList();

ll.insertStart(1)
ll.insertStart(2)
ll.insertStart(3)
ll.insertEnd(10)
ll.remove(3)


ll.traverseList()
print(ll.size1())

