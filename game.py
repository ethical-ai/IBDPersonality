#Game class provides the grid for prisoners dilemma.

class Game:

	'''
	Construct a game by takes in payoffs for each cell
	Parameter:  v1, v2, v3, v4 are vectors that contain payoffs of both players.
	'''
	def __init__(self, v1, v2, v3, v4):
		self.grid = [[v1, v2],[v3, v4]]
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.v4 = v4


	'''
	Returns the payoffs for both player from their decisions. Player 1 always passes in 1 or 2 and 
	player 2 always passes in 3 or 4
	Parameter: decisions from both player
	Return: a list size of two with both players' payoffs
	'''
	def getPayOffs(self, decision1, decision2):
		decision1 = decision1 - 1
		decision2 = int((decision2/2))-1
		return self.grid[decision1][decision2]

	''' 
	Returns the grid 
	'''
	def grid(self):
		return self.grid

	'''
	Returns the strategies for both players to get the best outcome 
	Return: return the best outcome strategies of player1 and player2
	'''
	def bestOutcome(self):
		sv1 = sum(self.v1)
		sv2 = sum(self.v2)
		sv3 = sum(self.v3)
		sv4 = sum(self.v4)

		sumList = [sv1, sv2, sv3, sv4]
		m = max(sumList)
		loc = sumList.index(m)

		if loc == 0:
			return [1,3]
		elif loc == 1:
			return [2,3]
		elif loc == 2:
			return [1,4]
		else:
			return [2,4]
