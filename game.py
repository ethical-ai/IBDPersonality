#Game class provides the grid for prisoners dilemma.

class Game:

	'''
	Construct a game by takes in payoffs for each cell
	Parameter:  v1, v2, v3, v4 are vectors that contain payoffs of both players.
	'''
	def __init__(self, v1, v2, v3, v4):
		self.grid = [[v1, v2],[v3, v4]]


	'''
	Returns the payoffs for both player from their decisions
	Parameter: decisions from both player
	Return: a list size of two with both players' payoffs
	'''
	def getPayOffs(self, decision1, decision2):
		return self.grid[decision1][decision2]

	''' 
	Returns the grid 
	'''
	def grid(self):
		return self.grid

