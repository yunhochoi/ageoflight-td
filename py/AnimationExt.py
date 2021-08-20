class AnimationExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.constant_cross_swap = self.ownerComp.op('constant_cross_swap')

		# camera motion
		self.CameraTy = 25
		self.CameraTz = 20
		self.CameraDistanceBegin = 7
		self.CameraDistanceEnd = 1
		self.CameraFOVBegin = 45
		self.CameraFOVEnd = 30


	def SwapParticleTree(self):

		self.ownerComp.op('constant_cross_swap').par.value0 = abs(self.ownerComp.op('constant_cross_swap').par.value0-1)