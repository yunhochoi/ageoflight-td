class AnimationExt:
	
	def __init__(self, ownerComp):

		# Operators
		self.ownerComp = ownerComp
		self.constant_cross_swap = self.ownerComp.op('constant_cross_swap')

		''' 인의예지 text'''
		self.FontSize = 20

		# position
		self.TextDistanceX = 480
		self.TextDistanceY = 240
		''' camera motion '''
		# 카메라가 바라보는 지점 높이
		self.CameraLookAtTyBegin = 10.5
		self.CameraLookAtTyFull = 12
		self.CameraLookAtTyEnd = 15

		# Fixed - please do not adjust
		self.CameraTy = 20
		self.CameraTx = -30

		# Camera distance
		self.CameraTzBegin = 10
		self.CameraTzFull = 30
		self.CameraTzEnd = 30


		# 횡으로 이동하는 모션 값
		self.CameraLateralBegin = 1
		self.CameraLateralFull = 1.7
		self.CameraLateralEnd = 2.6

		# 화각 (줌)
		self.CameraFOVBegin = 50
		self.CameraFOVFull = 60
		self.CameraFOVEnd = 12

		# Fixed - please do not adjust
		self.CameraPathBegin = 0
		self.CameraPathFull = 0
		self.CameraPathEnd = 0

		# particle mode update - 파티클 모드 바뀌는 시간
		self.ParticleModeLength = 15
		self.SwapLength = 3


	def SwapParticleTree(self):

		self.ownerComp.op('constant_cross_swap').par.value0 = abs(self.ownerComp.op('constant_cross_swap').par.value0-1)