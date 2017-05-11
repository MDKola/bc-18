class BinarySearch(list):
	#BinarySearch inherits from builtin list class
	def __init__(self,length,step):
		#__init__ takes in takes length and step as arguements
		super(BinarySearch,self).__init__()
		#super class initialized
		for item in range(1,length+1):
			self.append(item*step)

			self.length=len(self)

	def search(self,val):
		#performs a binary search to locate value
		first = 0
		last = len(self) - 1
		value_index = 0
		found = False

		counter = 0
		#counter initialized to zero

		#checking position of value
		if val==self[first]:
			value_index = first
			found = True
		elif val == self[last]:
			value_index = last
			found = True

		#making sure val is in list
		if val not in self:
			found = True
			value_index = -1