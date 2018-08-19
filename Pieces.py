# pieces
from Classes import *

# black pieces
black_a_rook = Rook("black", (0, 0))
black_b_knight = Knight("black", (0, 1))
black_c_bishop = Bishop("black", (0, 2))
black_d_queen = Queen("black", (0, 3))
black_e_king = King("black", (0, 4))
black_f_bishop = Bishop("black", (0, 5))
black_g_knight = Knight("black", (0, 6))
black_h_rook = Rook("black", (0, 7))

black_a_pawn = Pawn("black", (1, 0))
black_b_pawn = Pawn("black", (1, 1))
black_c_pawn = Pawn("black", (1, 2))
black_d_pawn = Pawn("black", (1, 3))
black_e_pawn = Pawn("black", (1, 4))
black_f_pawn = Pawn("black", (1, 5))
black_g_pawn = Pawn("black", (1, 6))
black_h_pawn = Pawn("black", (1, 7))


# white pieces
white_a_rook = Rook("white", (7, 0))
white_b_knight = Knight("white", (7, 1))
white_c_bishop = Bishop("white", (7, 2))
white_d_queen = Queen("white", (7, 3))
white_e_king = King("white", (7, 4))
white_f_bishop = Bishop("white", (7, 5))
white_g_knight = Knight("white", (7, 6))
white_h_rook = Rook("white", (7, 7))

white_a_pawn = Pawn("white", (6, 0))
white_b_pawn = Pawn("white", (6, 1))
white_c_pawn = Pawn("white", (6, 2))
white_d_pawn = Pawn("white", (6, 3))
white_e_pawn = Pawn("white", (6, 4))
white_f_pawn = Pawn("white", (6, 5))
white_g_pawn = Pawn("white", (6, 6))
white_h_pawn = Pawn("white", (6, 7))

pieces = (black_a_rook,
          black_b_knight,
          black_c_bishop,
          black_d_queen,
          black_e_king,
          black_f_bishop,
          black_g_knight,
          black_h_rook,
          black_a_pawn,
          black_b_pawn,
          black_c_pawn,
          black_d_pawn,
          black_e_pawn,
          black_f_pawn,
          black_g_pawn,
          black_h_pawn,

          white_a_rook,
          white_b_knight,
          white_c_bishop,
          white_d_queen,
          white_e_king,
          white_f_bishop,
          white_g_knight,
          white_h_rook,
          white_a_pawn,
          white_b_pawn,
          white_c_pawn,
          white_d_pawn,
          white_e_pawn,
          white_f_pawn,
          white_g_pawn,
          white_h_pawn,
          )
