import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.symbols = {"Player 1": "X", "Player 2": "O"}
        self.current_player = "Player 1"
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
    
    def create_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(self.root, text=" ", font=("Arial", 20), height=2, width=5,
                                               command=lambda row=r, col=c: self.make_move(row, col))
                self.buttons[r][c].grid(row=r, column=c)
    
    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.symbols[self.current_player]
            self.buttons[row][col].config(text=self.symbols[self.current_player])
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_board()
                return
            
            if self.is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
                return
            
            self.switch_player()
    
    def switch_player(self):
        self.current_player = "Player 1" if self.current_player == "Player 2" else "Player 2"
    
    def check_winner(self):
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
    
    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.board[r][c] = " "
                self.buttons[r][c].config(text=" ")
        self.current_player = "Player 1"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
