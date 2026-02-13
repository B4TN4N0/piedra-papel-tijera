from enum import Enum

class GameAction(Enum):
    Rock = "rock" #0
    Paper = "paper" #1
    Scissors = "scissors" #2
    Lizard = "lizard" #3
    Spock = "spock" #4

    @classmethod
    def minus(cls, *actions):
        return set(cls) - set(actions) # devuelve las acciones que no están en el conjunto de acciones (todas menos las especificadas)

class GameResult:
    Victory = "victory"
    Defeat = "defeat"
    Tie = "tie"

class Game:

    def __init__(self):
        # Game actions
        self.rock = GameAction.Rock
        self.paper = GameAction.Paper
        self.scissors = GameAction.Scissors
        self.lizard = GameAction.Lizard
        self.spock = GameAction.Spock
        # Game results
        self.victory = GameResult.Victory
        self.defeat = GameResult.Defeat
        self.tie = GameResult.Tie


    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            return self.tie

        wins = {
            self.rock: {self.scissors, self.lizard},
            self.paper: {self.rock, self.spock},
            self.scissors: {self.paper, self.lizard},
            self.lizard: {self.spock, self.paper},
            self.spock: {self.scissors, self.rock},
        }

        return self.victory if computer_action in wins.get(user_action, set()) else self.defeat
