#FIFO

class Queue:

	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue==[]

	def enqueue(self,data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def sizeQueue(self):
		return len(self.queue)


queue = Queue()

queue.enqueue(10)
print("Size: ",queue.sizeQueue())
queue.enqueue(20)
print("Size: ",queue.sizeQueue())
queue.enqueue(30)
print("Size: ",queue.sizeQueue())
queue.dequeue()
print("Size: ",queue.sizeQueue())
