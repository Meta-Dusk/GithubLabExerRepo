import random
import oxo_data

class Game:
    def __init__(self):
        """Start a new game with an empty board."""
        self.board = [" "] * 9  # 3x3 board

    def save(self):
        """Save the current game state."""
        oxo_data.saveGame(self.board)

    def load(self):
        """Load a saved game or start a new one."""
        self.board = oxo_data.restoreGame() if len(oxo_data.restoreGame()) == 9 else [" "] * 9

    def show_board(self):
        """Display the board."""
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)

    def check_winner(self):
        """Check if someone won."""
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                return self.board[a]  # Return 'X' or 'O'
        return None

    def player_move(self, cell):
        """Let the player move."""
        if self.board[cell] == " ":
            self.board[cell] = "X"
            return self.check_winner()

    def computer_move(self):
        """Let the computer make a random move."""
        options = [i for i in range(9) if self.board[i] == " "]
        if options:
            self.board[random.choice(options)] = "O"
            return self.check_winner()
        return "D"  # Draw

def play():
    """Run a simple test game."""
    game = Game()
    game.show_board()
    result = None

    while not result:
        result = game.player_move(random.choice([i for i in range(9) if game.board[i] == " "]))
        if not result:
            result = game.computer_move()

        game.show_board()
        if result:
            print("Winner:", result if result != "D" else "It's a draw!")

if __name__ == "__main__":
    play()

