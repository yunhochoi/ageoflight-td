class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp
		self.feedback_posBuffer = self.ownerComp.op('base_trees/geo_jung/feedback_posBuffer')
		self.feedback_velBuffer = self.ownerComp.op('base_trees/geo_jung/feedback_velBuffer')

		# attributes:
		self.NumDan = 4
		self.DanDistance = 1.6
		self.DanOffsetRangePosition = 0.3
		self.DanOffsetRangeHeight = 5
		self.DanOffsetRangeGravity = 5
		self.TruckHeight = 12
		self.TruckPoint = 5
		self.ParticleHeight = 10
	
		


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


	def HideParticles(self):
		print('hide')
		self.feedback_posBuffer.par.reset = True
		self.feedback_velBuffer.par.reset = True


	def ShowParticles(self):
		print('show')
		self.feedback_posBuffer.par.reset = False
		self.feedback_velBuffer.par.reset = False