import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        root.title("Tic Tac Toe")
        root.configure(bg="#1e1e1e")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 16), fg="white", bg="#1e1e1e")
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.root, text="", font=("Arial", 28), width=5, height=2,
                    command=lambda r=row, c=col: self.click(r, c),
                    bg="#2e2e2e", fg="white", activebackground="#3e3e3e", activeforeground="white"
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

    def click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                self.end_game(f"Player {self.current_player} wins!")
            elif self.check_draw():
                self.end_game("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)) or \
           all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_board()

    def reset_board(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.status_label.config(text="Player X's Turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state=tk.NORMAL)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
