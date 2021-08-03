import json
import logging 
import traceback
from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions


class DataExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.tree = op.Tree
		self.particle = op.Particle
		self.null_json = self.ownerComp.op('null_json')
		self.webclient_data = self.ownerComp.op('webclient_data')

		# attributes

		# Initializations
		run("op.Data.op('webclient_data').par.request.pulse()",fromOP = me, delayFrames = me.time.rate)


	def ParseJSON(self):

		# load and send message
		message = self.null_json.text

		if len(message) > 0:

			# load conductor message/command
			payload = json.loads(message)
			
			# raw message dump/display
			self.ownerComp.op('text_json').text = json.dumps(payload, sort_keys=True, indent=4)

			# Process data
			self.routeData(**payload)


	def routeData(self, **kwargs):
		
		wind = kwargs.get('wind', None)
		danTotal = kwargs.get('danTotal', None)
		posts = kwargs.get('posts', None)

		self.particle.op('base_process/table_jung_0').clear()
		self.particle.op('base_process/table_jung_1').clear()

		for jung in range(10):

			self.particle.op('base_process/table_jung_0').appendRows([posts[jung]['jung'][0]])
			self.particle.op('base_process/table_jung_1').appendRows([posts[jung]['jung'][1]])



		
		