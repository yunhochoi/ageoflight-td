class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp
		self.geo_trees = self.ownerComp.op('geo_trees')

		# attributes:
		self.NumDan = 3
		self.NumTree = 12
		self.DanDistance = 10
		self.DanDistanceOffset = 20
		self.TruckHeight = 10
		self.TruckPoint = 10


	def RandomizeTreeShape(self):

		for dan in range(4):
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_offsetX'.format(dan)).par.randomize.pulse()
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_seed'.format(dan)).par.randomize.pulse()
