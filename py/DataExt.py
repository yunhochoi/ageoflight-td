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
		self.colorLookup = {'1': [null_color['r'][0], null_color['g'][0], null_color['b'][0]],
							'2': [null_color['r'][1], null_color['g'][1], null_color['b'][1]],
							'3': [null_color['r'][2], null_color['g'][2], null_color['b'][2]],
							'4': [null_color['r'][3], null_color['g'][3], null_color['b'][3]],
							'5': [null_color['r'][4], null_color['g'][4], null_color['b'][4]],
							'6': [null_color['r'][5], null_color['g'][5], null_color['b'][5]],
							'7': [null_color['r'][6], null_color['g'][6], null_color['b'][6]]
							
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
		# self.Jung1 = []
		
		wind = kwargs.get('wind', None)
		danTotal = kwargs.get('danTotal', None)
		posts = kwargs.get('posts', None)
		
		null_color = self.particle.op('base_process/null_color')
		table_color = self.particle.op('base_process/table_color')
		self.particle.op('base_process/table_jung_0').clear()
		self.particle.op('base_process/table_jung_1').clear()
		
		table_color.clear()

		for jung in range(10):

			self.particle.op('base_process/table_jung_0').appendRows([posts[jung]['jung'][0]])
			self.particle.op('base_process/table_jung_1').appendRows([posts[jung]['jung'][1]])

			# print(self.colorLookup[str(posts[jung]['jung'][0])])
			self.Jung0.append(self.colorLookup[str(posts[jung]['jung'][0])])
			# self.Jung1.append(self.colorLookup[str(posts[jung]['jung'][1])])

		# print(self.Jung1[0])

		# self.particle.op('base_process/script_jung_0').setuppars.pulse()
		
			
		
			
			
		# table_color.appendCols(self.colorLookup[str(posts[jung]['jung'][0])], self.colorLookup[str(posts[jung]['jung'][1])], self.colorLookup[str(posts[jung]['jung'][0])])
		# table_color.appendCols([[null_color['r'][posts[0]['jung'][0]]]], 0)
		# table_color.appendCols([[null_color['r'][posts[0]['jung'][0]]]], 1)
		
		
	def SetupJung0Color(self, scriptOp):

		scriptOp.clear()
		# scriptOp.numSamples = scriptOp.inputs[0].numSamples
		scriptOp.numSamples = len(self.Jung0)
		r = scriptOp.appendChan('r')
		g = scriptOp.appendChan('g')
		b = scriptOp.appendChan('b')


	def CookJung0Color(self, scriptOp):

		r = scriptOp['r']
		g = scriptOp['g']
		b = scriptOp['b']
		
		for sample in range(0, scriptOp.numSamples):
			r[sample] = self.Jung0[sample][0] * 255
			g[sample] = self.Jung0[sample][1] * 255
			b[sample] = self.Jung0[sample][2] * 255

	
	# def SetupJung1Color(self, scriptOp):

	# 	scriptOp.clear()
	# 	scriptOp.numSamples = scriptOp.inputs[0].numSamples
	# 	r = scriptOp.appendChan('r')
	# 	g = scriptOp.appendChan('g')
	# 	b = scriptOp.appendChan('b')


	# def CookJung1Color(self, scriptOp):

	# 	r = scriptOp['r']
	# 	g = scriptOp['g']
	# 	b = scriptOp['b']
		
		# for sample in range(0, scriptOp.numSamples):
		# 	r[sample] = self.Jung1[sample][0] * 255
		# 	g[sample] = self.Jung1[sample][1] * 255
		# 	b[sample] = self.Jung1[sample][2] * 255
			



		
		