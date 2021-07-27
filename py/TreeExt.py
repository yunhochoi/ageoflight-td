class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp
		self.geo_trees = self.ownerComp.op('geo_trees')

		# attributes:
		self.NumDan = 3
		self.DanDistance = 4
		self.DanOffsetRangePosition = 2
		self.DanOffsetRangeHeight = 5
		self.DanOffsetRangeGravity = 20
		self.TruckHeight = 8
		self.TruckPoint = 10

	def CreateTrees(self):
	
		for dan in range(4):
			self.geo_trees.op('geo_dan_{}/replicator_tree'.format(dan)).par.recreateall.pulse()


	def RandomizeTreeShape(self):

		for dan in range(4):
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_offsetX'.format(dan)).par.randomize.pulse()
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_offsetX'.format(dan)).par.randomize.pulse()
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_seed_offset'.format(dan)).par.randomize.pulse()
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_seed_truck'.format(dan)).par.randomize.pulse()
			self.geo_trees.op('geo_dan_{}/base_shape/pattern_seed_lsystem'.format(dan)).par.randomize.pulse()
