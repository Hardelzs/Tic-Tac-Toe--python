class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.symbols = {}
        self.current_player = None

    def display_intro(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Rules: Players take turns placing X or O on the board. The first to get three in a row wins.")

    def display_board(self):
        print("\n---+---+---")
        for row in self.board:
            print(" | ".join(row))
            print("---+---+---")

    def set_symbols(self):
        symbol_1 = input("Player 1, choose X or O: ").upper()
        symbol_2 = "O" if symbol_1 == "X" else "X"
        self.symbols = {"Player 1": symbol_1, "Player 2": symbol_2}
        self.current_player = "Player 1"

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " "

    def make_move(self):
        while True:
            try:
                row = int(input(f"{self.current_player}, pick a row (0-2): "))
                col = int(input(f"{self.current_player}, pick a column (0-2): "))
                if self.is_valid_move(row, col):
                    self.board[row][col] = self.symbols[self.current_player]
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Enter a valid number.")

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = "Player 1" if self.current_player == "Player 2" else "Player 2"

    def play_game(self):
        self.display_intro()
        self.set_symbols()
        self.display_board()

        for turn in range(9):
            self.make_move()
            self.display_board()

            if self.check_winner():
                print(f"Congratulations! {self.current_player} wins!")
                return
            self.switch_player()

        print("It's a tie!")


# Run the game
game = TicTacToe()
game.play_game()
