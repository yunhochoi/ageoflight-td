

class ParticleExt:
	
	def __init__(self, ownerComp):
	
		# Operators
		self.ownerComp = ownerComp
		self.table_jung = ownerComp.op('table_jung')

		# attributes:

