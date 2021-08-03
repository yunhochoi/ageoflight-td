from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions


class ParticleExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
        # self.data = op.Data

		# attributes
		null_color = self.ownerComp.op('base_process/null_color')
		self.colorLookup = {'1': [null_color['r'][0], null_color['g'][0], null_color['b'][0]],
							'2': [null_color['r'][1], null_color['g'][1], null_color['b'][1]],
							'3': [null_color['r'][2], null_color['g'][2], null_color['b'][2]],
							'4': [null_color['r'][3], null_color['g'][3], null_color['b'][3]],
							'5': [null_color['r'][4], null_color['g'][4], null_color['b'][4]],
							'6': [null_color['r'][5], null_color['g'][5], null_color['b'][5]],
							'7': [null_color['r'][6], null_color['g'][6], null_color['b'][6]]
							
						   }

	def SetupJung0Color(self, scriptOp):

		scriptOp.clear()
		# scriptOp.numSamples = scriptOp.inputs[0].numSamples
		scriptOp.numSamples = len(op.Data.Jung0)
		r = scriptOp.appendChan('r')
		g = scriptOp.appendChan('g')
		b = scriptOp.appendChan('b')


	def CookJung0Color(self, scriptOp):

		r = scriptOp['r']
		g = scriptOp['g']
		b = scriptOp['b']
		
		for sample in range(0, scriptOp.numSamples):
			r[sample] = op.Data.Jung0[sample][0] * 255
			g[sample] = op.Data.Jung0[sample][1] * 255
			b[sample] = op.Data.Jung0[sample][2] * 255