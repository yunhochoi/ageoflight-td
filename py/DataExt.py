class DataExt:
	

	def __init__(self, ownerComp):
		# Operators
		self.ownerComp = ownerComp
		self.lsystem = op.Lsystem
		self.webclient_data = self.ownerComp.op('webclient_data')

		# attributes:

		# Initializations
		self.webclient_data.par.request.pulse()

	def OnRequest(self):

		self.lsystem.StartGrowth()
		