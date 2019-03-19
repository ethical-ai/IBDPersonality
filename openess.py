from random import randint
class Openness:

	# contruct a random player with specified number of player
	def __init__(self, player):
		self.player = player

	#random player always returns a random number between 0 and 1
	def play(self):
		if self.player == 1:
			return randint(0, 1)
		else: 
			return randint(2,3)

