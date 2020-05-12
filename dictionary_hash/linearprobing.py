
class HashTable(object):

	def __init__(self):
		self.size=10
		self.keys = [None]*self.size
		self.values = [None]*self.size

	#Put method: get a key and the value (data) and will insert it into the associative array
	#Using Linear probing (open adressing) for collisions
	def put(self, key, data):
		index = self.hashfunction(key)

		#not None -> it is a collision
		while self.keys[index] is not None:
			if self.keys[index] == key:
				self.values[index] = data
				return

			#rehash try to find another slot
			index = (index+1)%self.size
		#insert
		self.keys[index] = key
		self.values[index] = data

	def get(self, key):
		index = self.hashfunction(key)

		while self.keys[index] is not None:
			if self.keys[index]==key:
				return self.values[index]

			index = (index+1)%self.size

		#it means key is nor present in the associative array
		return None




	def hashfunction(self, key):
		sum=0
		for pos in range(len(key)):
			sum = sum+ord(key[pos])

		return sum%self.size