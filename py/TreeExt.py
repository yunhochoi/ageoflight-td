class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp
		self.geo_trees = self.ownerComp.op('geo_trees')

		# attributes:
		self.NumDan = 5
		self.DanDistance = 4
		self.DanOffsetRangePosition = 2
		self.DanOffsetRangeHeight = 5
		self.DanOffsetRangeGravity = 20
		self.TruckHeight = 8
		self.TruckPoint = 10

	
	def CreateTrees(self):
	
		self.RandomizeTreeShape()
		self.geo_trees.op('geo_dan_0/replicator_tree').par.recreateall.pulse()
		self.geo_trees.op('geo_dan_1/replicator_tree').par.recreateall.pulse()
		self.geo_trees.op('geo_dan_2/replicator_tree').par.recreateall.pulse()
		self.geo_trees.op('geo_dan_3/replicator_tree').par.recreateall.pulse()
		


	def RandomizeTreeShape(self):

		self.geo_trees.op('geo_dan_0/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.geo_trees.op('geo_dan_0/base_shape/pattern_seed_truck').par.randomize.pulse()
		self.geo_trees.op('geo_dan_0/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		self.geo_trees.op('geo_dan_1/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.geo_trees.op('geo_dan_1/base_shape/pattern_seed_truck').par.randomize.pulse()
		self.geo_trees.op('geo_dan_1/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		self.geo_trees.op('geo_dan_2/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.geo_trees.op('geo_dan_2/base_shape/pattern_seed_truck').par.randomize.pulse()
		self.geo_trees.op('geo_dan_2/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		self.geo_trees.op('geo_dan_3/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.geo_trees.op('geo_dan_3/base_shape/pattern_seed_truck').par.randomize.pulse()
		self.geo_trees.op('geo_dan_3/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		
