import tkinter as tk
from tkinter import messagebox

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = ""
SIZE = 3

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = PLAYER_X
        self.board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
        self.buttons = [[None for _ in range(SIZE)] for _ in range(SIZE)]
        self.create_board()

    def create_board(self):
        for row in range(SIZE):
            for col in range(SIZE):
                button = tk.Button(self.root, text=EMPTY, font=('consolas', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row.count(self.current_player) == SIZE:
                return True
        # Check columns
        for col in range(SIZE):
            if all(self.board[row][col] == self.current_player for row in range(SIZE)):
                return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(SIZE)):
            return True
        if all(self.board[i][SIZE-i-1] == self.current_player for i in range(SIZE)):
            return True
        return False

    def check_draw(self):
        return all(self.board[row][col] != EMPTY for row in range(SIZE) for col in range(SIZE))

    def reset_game(self):
        self.current_player = PLAYER_X
        self.board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
        for row in range(SIZE):
            for col in range(SIZE):
                self.buttons[row][col].config(text=EMPTY)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
