class NodeExt:
	
	def __init__(self, ownerComp):
		# Operators
		self.ownerComp = ownerComp

		# attributes:
		self.CameraMotion = True
		self.Sculpture = False
		self.Night = False
		self.CameraDistance = 0

	def myFunction(self, v):
		debug(v)

	def PromotedFunction(self, v):
		debug(v)