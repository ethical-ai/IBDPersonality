#agreeableness personality always chooses the best outcome for everyone
class Agreeableness:

	# contruct a player with specified number of player
	def __init__(self, player):
		self.player = player

	#player with agreeableness personality always chooses the best outcome
	def play(self, game):
		strategy = game.bestOutcome()
		if self.player == 1:
			return strategy[0]
		else:
			return strategy[1]


