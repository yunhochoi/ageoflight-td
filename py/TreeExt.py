class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp

		# attributes:
		self.NumDan = 7
		self.DanDistance = 3
		self.DanOffsetRangePosition = 2
		self.DanOffsetRangeHeight = 2
		self.DanOffsetRangeGravity = 5
		self.TruckHeight = 8
		self.TruckPoint = 5


	def CreateTrees(self):

		self.ownerComp.op('base_trees/geo_dan_0/replicator_tree').par.recreateall.pulse()
		self.ownerComp.op('base_trees/geo_dan_1/replicator_tree').par.recreateall.pulse()
		self.ownerComp.op('base_trees/geo_dan_2/replicator_tree').par.recreateall.pulse()
		self.ownerComp.op('base_trees/geo_dan_3/replicator_tree').par.recreateall.pulse()
	

	def RandomizeTreeShape(self):

		self.ownerComp.op('base_trees/geo_dan_0/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_0/base_shape/pattern_seed_trunk').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_0/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		self.ownerComp.op('base_trees/geo_dan_1/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_1/base_shape/pattern_seed_trunk').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_1/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		self.ownerComp.op('base_trees/geo_dan_2/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_2/base_shape/pattern_seed_trunk').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_2/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		self.ownerComp.op('base_trees/geo_dan_3/base_shape/pattern_seed_offset').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_3/base_shape/pattern_seed_trunk').par.randomize.pulse()
		self.ownerComp.op('base_trees/geo_dan_3/base_shape/pattern_seed_lsystem').par.randomize.pulse()

		
