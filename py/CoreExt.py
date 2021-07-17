

class CoreExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp
		
		# attributes
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

	
	def myFunction(self, v):
		debug(v)

	def PromotedFunction(self, v):
		debug(v)