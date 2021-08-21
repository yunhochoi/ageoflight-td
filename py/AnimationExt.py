class AnimationExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.constant_cross_swap = self.ownerComp.op('constant_cross_swap')

		# text
		self.FontSize = 40
		self.TextDistanceX = 525
		self.TextDistanceY = 250

		# camera motion
		self.CameraLookAtTyBegin = 8
		self.CameraLookAtTyFull = 12
		self.CameraLookAtTyEnd = 15

		self.CameraTy = 20
		self.CameraTz = 30
		self.CameraTx = -30

		self.CameraLateralBegin = 1
		self.CameraLateralFull = 1.7
		self.CameraLateralEnd = 2.3

		self.CameraFOVBegin = 40
		self.CameraFOVFull = 60
		self.CameraFOVEnd = 10

		self.CameraPathBegin = 0
		self.CameraPathFull = 0
		self.CameraPathEnd = 0

		# particle mode update
		self.ParticleModeLength = 15


	def SwapParticleTree(self):

		self.ownerComp.op('constant_cross_swap').par.value0 = abs(self.ownerComp.op('constant_cross_swap').par.value0-1)