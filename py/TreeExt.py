class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp

		'''base_process'''
		self.GrowSpeed = 1
		self.GrowNormalize = 100
		self.GrowRangeMin = 1.5
		self.GrowRangeMax = 5.5
	
		'''base_trees'''
		# shapes
		self.NumDan = 10                   
		self.DanDistance = 1
		self.DanOffsetRangePosition = 1
		self.DanOffsetRangeHeight = 5
		self.DanOffsetRangeGravity = 10
		self.TrunkHeight = 12
		self.TrunkPoint = 5

		# lsystem parameters
		self.Contangl = 1
		self.Contlength = 1
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


	def RouteData(self, **kwargs):
		
		# show data
		posts = kwargs.get('posts', None)
		wind = kwargs.get('wind', None)
		danTotal = kwargs.get('danTotal', None)

		# print(len(posts))

	
	def InitLsystem(self):

		self.ownerComp.op('base_process/timer_grow_0').par.initialize.pulse()
		self.ownerComp.op('base_process/timer_grow_1').par.initialize.pulse()
		self.ownerComp.op('base_process/timer_grow_2').par.initialize.pulse()
		self.ownerComp.op('base_process/timer_grow_3').par.initialize.pulse()

	
	def StartGrowth(self):
		
		self.ownerComp.op('base_process/timer_grow_0').par.start.pulse()
		self.ownerComp.op('base_process/timer_grow_1').par.start.pulse()
		self.ownerComp.op('base_process/timer_grow_2').par.start.pulse()
		self.ownerComp.op('base_process/timer_grow_3').par.start.pulse()


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