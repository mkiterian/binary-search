class BinarySearch(list):
	def __init__ (self, a, b):
		#pass values to list init so that a list is created when class inits
		super().__init__([x for x in range(b, (a*b)+b, b)])

		#initialize an instance variable
		self.length = len(self)

	def search(self, number):
		min_index = 0 
		max_index = self.length - 1
		count = 0

		if self[min_index] == number:
			return {'count': count, 'index': min_index}
		elif self[max_index] == number:
			return {'count': count, 'index': max_index}
		else:
			for num in range(self.length):
				guess = int((min_index + max_index)/2)
				if self[guess] == number:
					return {'count': count, 'index': guess}
				elif self[guess] < number:
					if number not in self[guess:]:
						return {'count': count, 'index': -1}
					min_index = guess + 1
					if min_index == (self.length-1):
						return {'count': count, 'index': -1}
				else:
					max_index = guess - 1
				count += 1