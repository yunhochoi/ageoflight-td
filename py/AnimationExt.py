class AnimationExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.constant_cross_swap = self.ownerComp.op('constant_cross_swap')

		# text
		self.FontSize = 40
		self.TextDistanceX = 500
		self.TextDistanceY = 200

		# camera motion
		self.CamreaLookAtTy = 8

		self.CameraTy = 20
		self.CameraTz = 30
		self.CameraTx = -30

		self.CameraDistanceBegin = 1
		self.CameraDistanceFull = 1
		self.CameraDistanceEnd = 1

		self.CameraFOVBegin = 45
		self.CameraFOVFull = 45
		self.CameraFOVEnd = 45

		self.CameraPathBegin = 0
		self.CameraPathFull = 0
		self.CameraPathEnd = 0


	def SwapParticleTree(self):

		self.ownerComp.op('constant_cross_swap').par.value0 = abs(self.ownerComp.op('constant_cross_swap').par.value0-1)