from tkinter import *
import numpy as np

AUTHOR = "Shivank Sharma"
# adapted from :--  https://github.com/aqeelanwar/Tic-Tac-Toe/blob/master/main.py
size_of_board = 600
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
symbol_X_color = "#22CF07"
symbol_O_color = "#E91515"
Green_color = "#000000"


class TicTacToe:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board, bg='white')
        self.canvas.pack()
        self.window.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = np.zeros(shape=(3, 3))

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line(
                (i + 1) * size_of_board / 3, 0,
                (i + 1) * size_of_board / 3, size_of_board
            )
        for i in range(2):
            self.canvas.create_line(
                0, (i + 1) * size_of_board / 3,
                size_of_board, (i + 1) * size_of_board / 3
            )

    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = np.zeros(shape=(3, 3))

    def draw_O(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(
            grid_position[0] - symbol_size, grid_position[1] - symbol_size,
            grid_position[0] + symbol_size, grid_position[1] + symbol_size,
            width=symbol_thickness, outline=symbol_O_color
        )

    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(
            grid_position[0] - symbol_size, grid_position[1] - symbol_size,
            grid_position[0] + symbol_size, grid_position[1] + symbol_size,
            width=symbol_thickness, fill=symbol_X_color
        )
        self.canvas.create_line(
            grid_position[0] - symbol_size, grid_position[1] + symbol_size,
            grid_position[0] + symbol_size, grid_position[1] - symbol_size,
            width=symbol_thickness, fill=symbol_X_color
        )

    def display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            text = 'Winner: Player 1 (X)'
            color = symbol_X_color
        elif self.O_wins:
            self.O_score += 1
            text = 'Winner: Player 2 (O)'
            color = symbol_O_color
        else:
            self.tie_score += 1
            text = 'Its a tie'
            color = 'gray'

        self.canvas.delete("all")
        
        # Winner text
        self.canvas.create_text(
            size_of_board / 2, 80,
            font="cmr 50 bold", fill=color, text=text
        )

        # Scores header
        self.canvas.create_text(
            size_of_board / 2, 160,
            font="cmr 35 bold", fill=Green_color, text='Scores'
        )

        # Score details
        score_text = (
            f'Player 1 (X): {self.X_score}\n'
            f'Player 2 (O): {self.O_score}\n'
            f'Tie: {self.tie_score}'
        )
        self.canvas.create_text(
            size_of_board / 2, 270,
            font="cmr 24 bold", fill=Green_color, text=score_text,
            justify=CENTER
        )

        # Play again prompt
        self.canvas.create_text(
            size_of_board / 2, 500,
            font="cmr 18 bold", fill="gray", text='Click to play again'
        )
        self.reset_board = True

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (size_of_board / 3) * logical_position + size_of_board / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (size_of_board / 3), dtype=int)

    def is_grid_occupied(self, logical_position):
        return self.board_status[logical_position[0]][logical_position[1]] != 0

    def is_winner(self, player):
        player_value = -1 if player == 'X' else 1

        # Check rows and columns
        for i in range(3):
            if all(self.board_status[i][j] == player_value for j in range(3)):
                return True
            if all(self.board_status[j][i] == player_value for j in range(3)):
                return True

        # Check diagonals
        if all(self.board_status[i][i] == player_value for i in range(3)):
            return True
        if all(self.board_status[i][2-i] == player_value for i in range(3)):
            return True

        return False

    def is_tie(self):
        return np.count_nonzero(self.board_status == 0) == 0

    def is_gameover(self):
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')
        if not self.O_wins:
            self.tie = self.is_tie()

        return self.X_wins or self.O_wins or self.tie

    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = False
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = True

            if self.is_gameover():
                self.display_gameover()
        else:
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False


def run():
    game = TicTacToe()
    game.mainloop()

