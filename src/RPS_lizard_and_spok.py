from enum import Enum

class GameAction(Enum):
    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"
    Lizard = "lizard"
    Spock = "spock"

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
