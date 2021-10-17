class ParticleExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp

		# color control
		self.BlinkMode = 2   # 0: nothing, 1: blinking, 2: crossfading
		self.BlinkSpeed = 0.2
		self.BlinkAlphaNoise = False

		# particle shape
		self.NumParticle = 5000
		self.ParticleSize = 0.17
		
		self.ParticleScale = 7
		self.ParticleTy = 26
		self.SmoothFade = 0