class DataExt:
	

	def __init__(self, ownerComp):
		# Operators
		self.ownerComp = ownerComp
		self.webclient_data = self.ownerComp.op('webclient_data')

		# attributes:

		# Initializations
		self.webclient_data.par.request.pulse()

	def myFunction(self, v):
		debug(v)

	def PromotedFunction(self, v):
		debug(v)