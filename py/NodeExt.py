import json

class NodeExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp

		# attributes:
		self.CameraMotion = False
		self.Sculpture = False
		self.Night = True
		self.CameraDistance = 0

	def myFunction(self, v):
		debug(v)

	def PromotedFunction(self, v):
		debug(v)

	def ExportJSON(self, instanceOp):

		self.rootDictionary = {}
		self.samples = []

		for sample in range(0, instanceOp.numSamples):
		
			instanceData = {}
			
			for channel in instanceOp.chans():
				
				instanceData[channel.name] = instanceOp[channel.name][sample]
			
			self.samples.append(instanceData)
	
		with open('json/particlePosition.json', 'w') as outfile:
			
			json.dump(self.samples, outfile)
		

		return