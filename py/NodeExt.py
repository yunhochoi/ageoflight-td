class NodeExt:
	
	def __init__(self, ownerComp):
		# Operators
		self.ownerComp = ownerComp

		# attributes:
		self.CameraMotion = False
		self.Sculpture = True
		self.Night = False

	def myFunction(self, v):
		debug(v)

	def PromotedFunction(self, v):
		debug(v)