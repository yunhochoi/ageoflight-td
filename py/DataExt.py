class DataExt:
	

	def __init__(self, ownerComp):
		# Operators
		self.ownerComp = ownerComp
		self.lsystem = op.Lsystem
		self.tree = op.Tree
		self.webclient_data = self.ownerComp.op('webclient_data')

		# attributes:

		# Initializations
		run("op.Data.op('webclient_data').par.request.pulse()",fromOP = me, delayFrames = 2*me.time.rate)

	def OnRequest(self):

		self.tree.RandomizeTreeShape()
		self.lsystem.InitLsystem()
		self.lsystem.StartGrowth()
		self.tree.CreateTrees()
		
		
		
		