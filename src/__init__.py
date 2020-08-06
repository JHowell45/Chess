"""

"""
from random import randint


class Board:

    X_KEY = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }

    def __init__(self):
        self.turn_count = 0
        self.player_turn = True
        self.starting_colour_value = True if randint(0, 1) else False
        self.board = [["x" for _ in range(8)] for _ in range(8)]

        # starting_pieces = (
        #     {"king", "queen"}
        #     .union({f"bishop_{x}" for x in range(2)})
        #     .union({f"knight_{x}" for x in range(2)})
        #     .union({f"castle_{x}" for x in range(2)})
        #     .union({f"pawn_{x}" for x in range(8)})
        # )

        starting_pieces = (
            ["king", "queen"]
            + [f"bishop_{x}" for x in range(2)]
            + [f"knight_{x}" for x in range(2)]
            + [f"castle_{x}" for x in range(2)]
            + [f"pawn_{x}" for x in range(8)]
        )
        self.player_1 = starting_pieces
        self.player_2 = starting_pieces

        self.starting_positions()

    def player_colour(self):
        return "White" if self.starting_colour_value else "Black"

    def starting_positions(self):
        if self.starting_colour_value:
            first_row = 8
            second_row = 7
        else:
            first_row = 1
            second_row = 2
        self.place_piece(f"A{first_row}", self.player_1[6])
        self.place_piece(f"B{first_row}", self.player_1[4])
        self.place_piece(f"C{first_row}", self.player_1[2])
        self.place_piece(f"D{first_row}", self.player_1[1])
        self.place_piece(f"E{first_row}", self.player_1[0])
        self.place_piece(f"F{first_row}", self.player_1[3])
        self.place_piece(f"G{first_row}", self.player_1[5])
        self.place_piece(f"H{first_row}", self.player_1[7])

        self.place_piece(f"A{second_row}", self.player_1[8])
        self.place_piece(f"B{second_row}", self.player_1[9])
        self.place_piece(f"C{second_row}", self.player_1[10])
        self.place_piece(f"D{second_row}", self.player_1[11])
        self.place_piece(f"E{second_row}", self.player_1[12])
        self.place_piece(f"F{second_row}", self.player_1[13])
        self.place_piece(f"G{second_row}", self.player_1[14])
        self.place_piece(f"H{second_row}", self.player_1[15])

    def get_position(self, pos: str):
        x, y = list(pos)
        y = self.X_KEY[x.lower()]
        x = 7 - (int(y) - 1)
        return self.board[x][y]

    def place_piece(self, pos, piece):
        x, y = list(pos)
        print(x, y)
        true_y = self.X_KEY[x.lower()]
        true_x = 7 - (int(y) - 1)
        print(true_x, true_y)
        self.board[true_x][true_y] = piece

    def display_board(self):
        for index, row in enumerate(self.board):
            print(f"{8 - index}", end="")
            for col in row:
                print(f" {col} ", end="")
            print()
        for x in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            print(f" {x} ", end="")
        print()

    def __repr__(self):
        return (
            f"<Chess Board || Player Turn: {self.player_turn}, Player 1:"
            f" {self.player_1}, Player 2: {self.player_2}>"
        )


class Player:
    def __init__(self):
        pass
