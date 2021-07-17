import json

class LsystemExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.null_instance = ownerComp.op('null_instance')

		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

		# initializations
		self.samples = None

	def ExportJSON(self):

		self.samples = []

		for i in range(0, self.null_instance.numSamples):
		
			instanceData = {}
			
			for c in self.null_instance.chans():
				
				instanceData[c.name] = self.null_instance[c.name][i]
			
			self.samples.append(instanceData)
	
	
		with open('json/instances.json', 'w') as outfile:
			
			json.dump(self.samples, outfile)
		

		return

