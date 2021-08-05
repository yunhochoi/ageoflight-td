class ParticleExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp

		# color control
		self.BlinkMode = 2   # 0: nothing, 1: blinking, 2: crossfading
		self.BlinkSpeed = 0.2
		self.BlinkAlphaNoise = True

		# particle shape
		self.ParticleMaterial = 0    # 0: PBR, 1: phong, 2: constant 
		self.ParticleHeight = 37
		self.ParticleWidth = 6
		self.ParticleScale = 0.2
		self.ParticleFormScale = 1.2
		self.VerticalMove = 1


	def SetupParticleColor(self, scriptOp):

		scriptOp.clear()
		scriptOp.numSamples = scriptOp.inputs[0].numSamples
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
