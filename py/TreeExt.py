class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp

		'''base_process'''
		self.DummyData = False
		self.GrowSpeed = 2
		self.GrowNormalize = 100
		self.GrowRangeMin = 3.2
		self.GrowRangeMax = 4.1
	
		'''base_trees'''
		# num, position
		self.NumDan = 30
		self.DanDistance = 1
		self.DanOffsetRangePosition = 1.1
		self.DanOffsetRangeHeight = 2
		self.DanOffsetRangeGravity = 10

		# data driven trunk, branch shape
		self.LowTrunkHeight = 10
		self.HighTrunkLengthMin = 0.3
		self.HighTrunkLengthMax = 0.5
		self.TrunkPoint = 5
		self.HighTrunkRx = [ 30,  20, -20,  -30 ]
		self.BranchRx    = [ 45, -45, 45,  -45 ]
		self.HighTrunkRy = [ 0,  -90,  -90,   90 ]
		self.BranchRy    = [-30,  -35,  30,  30 ]
		self.HighTrunkRz = [-20,  20,  60,  -60 ]
		self.BranchRz    = [-90,  90,  90,  -90 ]

		# fixed trunk, branch shape
		self.NumFixedTrunk = 7
		self.FixedTrunkHeight = 3
		self.FixedTrunkScale = 2
		self.FixedTrunkScaleStep = [1.2, 1.0, 1.10]
		self.FixedTrunkPosStep = 0.5
		
		# lsystem parameters
		self.Contangl = 1
		self.Contlength = 0
		self.Angleinit = 100
		
		
	def CreateTrees(self):
		
		# recreate all trees 
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


	def ExportJSON(self):

		self.rootDictionary = {}
		self.samples = []

		for sample in range(0, self.null_instance.numSamples):
		
			instanceData = {}
			
			for channel in self.null_instance.chans():
				
				instanceData[channel.name] = self.null_instance[channel.name][sample]
			
			self.samples.append(instanceData)
	
		with open('json/lsystem.json', 'w') as outfile:
			
			json.dump(self.samples, outfile)
		

		return