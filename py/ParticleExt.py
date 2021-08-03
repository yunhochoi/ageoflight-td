class ParticleExt:
	
	def __init__(self, ownerComp):
	
		# Operators
		self.ownerComp = ownerComp

		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute


	def RouteData(self, **kwargs):
		
		# show data
		posts = kwargs.get('posts', None)
		wind = kwargs.get('wind', None)
		danTotal = kwargs.get('danTotal', None)

		print(len(posts))