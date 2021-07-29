import json

class DataExt:
	
	def __init__(self, ownerComp):
		# Operators
		self.ownerComp = ownerComp
		self.lsystem = op.Lsystem
		self.tree = op.Tree
		self.null_json = self.ownerComp.op('null_json')
		self.webclient_data = self.ownerComp.op('webclient_data')

		# attributes:

		# Initializations
		run("op.Data.op('webclient_data').par.request.pulse()",fromOP = me, delayFrames = 2*me.time.rate)

	# def OnRequest(self):

	# 	self.tree.RandomizeTreeShape()
	# 	self.lsystem.InitLsystem()
	# 	self.lsystem.StartGrowth()
	# 	self.tree.CreateTrees()

	def ParseJSON(self):

		# load and send message
		message = self.null_json.text

		if len(message) > 0:

			# load conductor message/command
			payload = json.loads(message)

			# raw message dump/display
			self.ownerComp.op('text_json').text = json.dumps(payload, sort_keys=True, indent=4)

			# Process data
			op.Tree.RouteData(**payload)



		
		