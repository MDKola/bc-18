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