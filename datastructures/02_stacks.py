class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack==[]

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		return self.stack[-1]

	def sizeStack(self):
		return len(self.stack)



stack = Stack()

stack.push(1)

print("Size:", stack.sizeStack())
stack.push(2)

print("Size:", stack.sizeStack())
stack.push(3)

print("Size:", stack.sizeStack())
stack.pop()

print("Size:", stack.sizeStack())