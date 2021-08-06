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
		null_color = self.particle.op('base_process/null_color')
		self.colorLookup = {
							'1': [null_color['r'][0], null_color['g'][0], null_color['b'][0]],
							'2': [null_color['r'][1], null_color['g'][1], null_color['b'][1]],
							'3': [null_color['r'][2], null_color['g'][2], null_color['b'][2]],
							'4': [null_color['r'][3], null_color['g'][3], null_color['b'][3]],
							'5': [null_color['r'][4], null_color['g'][4], null_color['b'][4]],
							'6': [null_color['r'][5], null_color['g'][5], null_color['b'][5]],
							'7': [null_color['r'][6], null_color['g'][6], null_color['b'][6]],
							'8': [null_color['r'][7], null_color['g'][7], null_color['b'][7]]
						   }

		self.Jung0 = []
		self.Jung1 = []

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

		self.Jung0 = []
		self.Jung1 = []
		
		wind = kwargs.get('wind', None)
		danTotal = kwargs.get('danTotal', None)
		jungTotal = kwargs.get('jungTotal', None)
		posts = kwargs.get('posts', None)

		null_color = self.particle.op('base_process/null_color')
		self.particle.op('base_process/table_jung_0').clear()
		self.particle.op('base_process/table_jung_1').clear()
		self.particle.op('base_process/table_jung_total').clear()

		for jung in range(1000):

			self.particle.op('base_process/table_jung_0').appendRows([posts[jung]['jung'][0]])
			self.particle.op('base_process/table_jung_1').appendRows([posts[jung]['jung'][1]])

			self.Jung0.append(self.colorLookup[str(posts[jung]['jung'][0])])
			self.Jung1.append(self.colorLookup[str(posts[jung]['jung'][1])])
			
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['a']])
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['b']])
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['c']])
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['d']])
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['e']])
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['f']])
		self.particle.op('base_process/table_jung_total').appendRows([jungTotal['g']])

		
		