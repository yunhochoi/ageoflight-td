class TreeExt:
	
	def __init__(self, ownerComp):
		
		# Operators
		self.ownerComp = ownerComp
		self.geo_tree = self.ownerComp.op('geo_tree')

		# attributes:
		self.NumDan = 3
		self.NumTree = 12
		self.DanDistance = 10
		self.DanDistanceOffset = 20
		self.TruckHeight = 10
		self.TruckPoint = 10


	def RandomizeTreeOffset(self):

		# op('base_offset/pattern_offsetX').par.randomize.pulse()
		# op('base_offset/pattern_offsetY').par.randomize.pulse()

		for dan in range(3):
			self.geo_tree.op('geo_dan_{}/base_offset/pattern_offsetX'.format(dan)).par.randomize.pulse()