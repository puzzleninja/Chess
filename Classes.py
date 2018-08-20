# classes
from References import *


class Piece:
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image


class Pawn(Piece):
    def __init__(self, color, pos):
        self.color = color
        image = ""
        if color == "white":
            image = white_pawn
        elif color == "black":
            image = black_pawn
        Piece.__init__(self, pos, image)

    def __str__(self):
        return self.color + " pawn"

    def get_moves(self, board):
        moves = []
        if self.color == "white":
            if self.pos[0] == 6:
                if not board[self.pos[0] - 1][self.pos[1]]:
                    moves.append((self.pos[0] - 1, self.pos[1]))
                    if not board[self.pos[0] - 2][self.pos[1]]:
                        moves.append((self.pos[0] - 2, self.pos[1]))
            else:
                if not board[self.pos[0] - 1][self.pos[1]]:
                    moves.append((self.pos[0] - 1, self.pos[1]))
            if self.pos[1] < 7:
                if board[self.pos[0] - 1][self.pos[1] + 1]:
                    if board[self.pos[0] - 1][self.pos[1] + 1].color == "black":
                        moves.append((self.pos[0] - 1, self.pos[1] + 1))
            if self.pos[1] > 0:
                if board[self.pos[0] - 1][self.pos[1] - 1]:
                    if board[self.pos[0] - 1][self.pos[1] - 1].color == "black":
                        moves.append((self.pos[0] - 1, self.pos[1] - 1))

        if self.color == "black":
            if self.pos[0] == 1:
                if not board[self.pos[0] + 1][self.pos[1]]:
                    moves.append((self.pos[0] + 1, self.pos[1]))
                    if not board[self.pos[0] + 2][self.pos[1]]:
                        moves.append((self.pos[0] + 2, self.pos[1]))
            else:
                if not board[self.pos[0] + 1][self.pos[1]]:
                    moves.append((self.pos[0] + 1, self.pos[1]))
            if self.pos[1] < 7:
                if board[self.pos[0] + 1][self.pos[1] + 1]:
                    if board[self.pos[0] + 1][self.pos[1] + 1].color == "white":
                        moves.append((self.pos[0] + 1, self.pos[1] + 1))
            if self.pos[1] > 0:
                if board[self.pos[0] + 1][self.pos[1] - 1]:
                    if board[self.pos[0] + 1][self.pos[1] - 1].color == "white":
                        moves.append((self.pos[0] + 1, self.pos[1] - 1))
        return moves


class Knight(Piece):
    def __init__(self, color, pos):
        self.color = color
        image = ""
        if color == "white":
            image = white_knight
        elif color == "black":
            image = black_knight
        Piece.__init__(self, pos, image)

    def __str__(self):
        return self.color + " knight"

    def get_moves(self, board):
        moves = []
        potential_relative_moves = [
            (-1, -2),
            (-2, -1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (1, 2),
            (2, 1)
        ]
        for move in potential_relative_moves:
            potential_move = (self.pos[0] + move[0], self.pos[1] + move[1])
            if 0 <= potential_move[0] < len(board) and 0 <= potential_move[1] < len(board[0]):
                if not board[potential_move[0]][potential_move[1]]:
                    moves.append(potential_move)
                else:
                    if board[potential_move[0]][potential_move[1]].color != self.color:
                        moves.append(potential_move)
        return moves


class Bishop(Piece):
    def __init__(self, color, pos):
        self.color = color
        image = ""
        if color == "white":
            image = white_bishop
        elif color == "black":
            image = black_bishop
        Piece.__init__(self, pos, image)

    def __str__(self):
        return self.color + " bishop"

    def get_moves(self, board):
        moves = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                tile = (self.pos[0], self.pos[1])
                for x in range(8):
                    tile = (tile[0] + i, tile[1] + j)
                    if 0 <= tile[0] < len(board) and 0 <= tile[1] < len(board[0]):
                        if not board[tile[0]][tile[1]]:
                            moves.append(tile)
                        elif board[tile[0]][tile[1]].color != self.color:
                            moves.append(tile)
                            break
                        else:
                            break
        return moves


class Rook(Piece):
    def __init__(self, color, pos):
        self.color = color
        image = ""
        if color == "white":
            image = white_rook
        elif color == "black":
            image = black_rook
        Piece.__init__(self, pos, image)

    def __str__(self):
        return self.color + " rook"

    def get_moves(self, board):
        moves = []
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            tile = (self.pos[0], self.pos[1])
            for x in range(8):
                tile = (tile[0] + i, tile[1] + j)
                if 0 <= tile[0] < len(board) and 0 <= tile[1] < len(board[0]):
                    if not board[tile[0]][tile[1]]:
                        moves.append(tile)
                    elif board[tile[0]][tile[1]].color != self.color:
                        moves.append(tile)
                        break
                    else:
                        break
        return moves


class Queen(Piece):
    def __init__(self, color, pos):
        self.color = color
        image = ""
        if color == "white":
            image = white_queen
        elif color == "black":
            image = black_queen
        Piece.__init__(self, pos, image)

    def __str__(self):
        return self.color + " queen"

    def get_moves(self, board):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                tile = (self.pos[0], self.pos[1])
                for x in range(8):
                    tile = (tile[0] + i, tile[1] + j)
                    if 0 <= tile[0] < len(board) and 0 <= tile[1] < len(board[0]):
                        if not board[tile[0]][tile[1]]:
                            moves.append(tile)
                        elif board[tile[0]][tile[1]].color != self.color:
                            moves.append(tile)
                            break
                        else:
                            break
        return moves


class King(Piece):
    def __init__(self, color, pos):
        self.color = color
        image = ""
        if color == "white":
            image = white_king
        elif color == "black":
            image = black_king
        Piece.__init__(self, pos, image)

    def __str__(self):
        return self.color + " king"

    def get_moves(self, board):
        moves = []
        return moves
