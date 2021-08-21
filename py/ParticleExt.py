class ParticleExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp

		# color control
		self.BlinkMode = 2   # 0: nothing, 1: blinking, 2: crossfading
		self.BlinkSpeed = 0.2
		self.BlinkAlphaNoise = False

		# particle shape
		self.NumParticle = 2000
		self.ParticleSize = 0.17
		self.ParticleScale = 1.37
		self.ParticleTy = 26
		self.SmoothFade = 0
		self.NoiseAlphaSpeed = 10
	