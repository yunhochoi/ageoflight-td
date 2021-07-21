import json

class LsystemExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.null_instance = ownerComp.op('null_instance')
		self.geo_lsystem_1 = ownerComp.op('geo_lsystem_1')
		self.geo_lsystem_2 = ownerComp.op('geo_lsystem_2')
		self.geo_lsystem_3 = ownerComp.op('geo_lsystem_3')
		self.geo_lsystem_4 = ownerComp.op('geo_lsystem_4')
		self.instanceArray = [self.geo_lsystem_1, self.geo_lsystem_2, self.geo_lsystem_3, self.geo_lsystem_4]

		# attributes
		self.samples = None
		self.rootDictionary = None
		self.Generations = 7
		self.Type = 'tube'


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

