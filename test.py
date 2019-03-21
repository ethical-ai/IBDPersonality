#import classes from other files in the same directory
from game import Game
from agreeableness import Agreeableness
from openess import Openness
from stability import Stability

#create a game
game = Game([1,1], [3,0], [0,3], [2,2])

#create 2 players
a1 = Openness(1)
o2 = Stability(2)

#p1: payoff for player1 and p2: payoff for player2
p1 = 0
p2 = 0


#Note: agreeableness's playe method requires game

for i in range(10):
	s1 = a1.play()
	s2 = o2.play()
	payoffs = game.getPayOffs(s1,s2)
	p1 += payoffs[0]
	p2+=payoffs[1]
	
print(p1)
print(p2)

