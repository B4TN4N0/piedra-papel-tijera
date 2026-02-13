from enum import Enum

class GameAction(Enum):
    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"

class GameResult:
    Victory = "victory"
    Defeat = "defeat"
    Tie = "tie"

class RPSGame:

    def __init__(self):
        # Game actions
        self.rock = GameAction.Rock
        self.paper = GameAction.Paper
        self.scissors = GameAction.Scissors
        # Game results
        self.victory = GameResult.Victory
        self.defeat = GameResult.Defeat
        self.tie = GameResult.Tie

    def assess_game(self, user_action, computer_action):
        if user_action == computer_action:
            return self.tie
        elif (user_action == self.rock and computer_action == self.scissors) or \
            (user_action == self.paper and computer_action == self.rock) or \
            (user_action == self.scissors and computer_action == self.paper):
            return self.victory
        else:
            return self.defeat

    
