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
							'7': [null_color['r'][6], null_color['g'][6], null_color['b'][6]],
							'8': [null_color['r'][7], null_color['g'][7], null_color['b'][7]]
							
						   }

	def SetupParticleColor(self, scriptOp):

		scriptOp.clear()
		scriptOp.numSamples = scriptOp.inputs[0].numSamples
		# scriptOp.numSamples = len(op.Data.Jung0)
		jung_0_r = scriptOp.appendChan('jung_0_r')
		jung_0_g = scriptOp.appendChan('jung_0_g')
		jung_0_b = scriptOp.appendChan('jung_0_b')
		jung_1_r = scriptOp.appendChan('jung_1_r')
		jung_1_g = scriptOp.appendChan('jung_1_g')
		jung_1_b = scriptOp.appendChan('jung_1_b')


	def CookParticleColor(self, scriptOp):

		jung_0_r = scriptOp['jung_0_r']
		jung_0_g = scriptOp['jung_0_g']
		jung_0_b = scriptOp['jung_0_b']
		jung_1_r = scriptOp['jung_1_r']
		jung_1_g = scriptOp['jung_1_g']
		jung_1_b = scriptOp['jung_1_b']
		
		for sample in range(0, scriptOp.numSamples):
			jung_0_r[sample] = op.Data.Jung0[sample][0] / 255
			jung_0_g[sample] = op.Data.Jung0[sample][1] / 255
			jung_0_b[sample] = op.Data.Jung0[sample][2] / 255
			jung_1_r[sample] = op.Data.Jung1[sample][0] / 255
			jung_1_g[sample] = op.Data.Jung1[sample][1] / 255
			jung_1_b[sample] = op.Data.Jung1[sample][2] / 255
