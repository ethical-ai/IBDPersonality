# Ethical AI

This project aims to use the ideas presented by Yijia Wang, Yan Wan and Zhijian Wang in "Using experimental game theory to transit human values to ethical AI" to explore how different personality types may fare in an iterated prisoners dilemma game. The project simulates openness, agreeableness, and instability, calculating how players with these personality traits may play in a game.
An open player might switch strategies often in order to attempt a better result, an agreeable personality might always choose what's best for everyone, and an unstable player would default to random choices if they were on a loosing streak. By exploring how these personalities interact, we hope to draw conclusions about the use of game theory in determining how to judge ethics in interactions between different personalities.

Our program sets up a prisoner's dilemma game with the following board, with 1, 2, 3, and 4 representing the vectors with the payoffs of both players:

            |  P1   |
            |   C   |   D  
      P2  C |   1   |   2  
          D |   3   |   4  

 
When the iterated game is run, each player's payoffs will be calculated every round and added together to get a final score.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Prerequisites

Our simulation runs on Python.

## Running the tests

...

## Built With

* [Sublime](https://www.sublimetext.com/) - The Python editor used.

## Authors

* **Ching-Ching Huang** - *Code Manager*
* **Elijah Friedrich** - *Experimentalist*
* **Sophie Li** - *Researcher*
* **Stephen de Riel** - *Reporter*

