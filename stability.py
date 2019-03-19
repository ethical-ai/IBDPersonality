'''
Stability personlity always choose the best strategy for him/herself
'''
class Stability:

	# contruct a random player with specified number of player
	def __init__(self, player):
		self.player = player

	#  alwyas confess
	def play(self, player):
		if self.player == 1:
			return 2
		else: 
			return 4



