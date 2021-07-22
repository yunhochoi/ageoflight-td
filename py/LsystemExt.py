import json

class LsystemExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.null_instance = self.ownerComp.op('null_instance')
		self.timer_grow_0 = self.ownerComp.op('base_grow/timer_grow_0')
		self.timer_grow_1 = self.ownerComp.op('base_grow/timer_grow_1')
		self.timer_grow_2 = self.ownerComp.op('base_grow/timer_grow_2')
		self.timer_grow_3 = self.ownerComp.op('base_grow/timer_grow_3')

		# attributes
		self.samples = None
		self.rootDictionary = None
		
		self.numDan = 4
		self.Generations = 0
		self.GrowSpeed = 1
		self.GrowNormalize = 100
		self.GrowRange = 4
		self.Type = 'skel'


	def InitLsystem(self):
		for dan in range(0, self.numDan-1):
			self.ownerComp.op('base_grow/timer_grow_{}'.format(dan)).par.initialize.pulse()
			
	
	def StartGrowth(self):
		
		for dan in range(0, self.numDan-1):
			self.ownerComp.op('base_grow/timer_grow_{}'.format(dan)).par.start.pulse()

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

