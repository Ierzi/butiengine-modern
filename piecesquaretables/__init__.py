"""The Piece Square Tables for all the pieces in chess."""
# This piece square table was made uniquely for ButiEngine Modern
WHITE_KING = (
    (-10, -10, -10, -10, -10, -10, -10, -10),
    (2, 1, 0, 0, 0, 0, 1, 2),
    (2, 1, 0, 0, 0, 0, 1, 2),
    (2, 1, 0, 0, 0, 0, 1, 2),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1.2, 0, 0, 0, 0, 0, 1.2),
    (2, 3, 2, 1, 1, 1, 3, 2),
    (5, 10, 10, 5.5, 5.5, 10, 10, 5)
)

BLACK_KING = reversed(WHITE_KING)

# This one was made for the original ButiEngine, just made some tweaks
WHITE_PAWN_OPENING = (
    (0, 0, 0, 0, 0, 0, 0, 0),
    (5, 10, 10, -20, -20, 10, 10, 5),
    (5, -5, -5, 5, 5, -5, -5, 5),
    (0, 0, 0, 25, 25, 0, 0, 0),
    (5, 5, 10, 25, 25, 10, 5, 5),
    (10, 10, 20, 30, 30, 20, 10, 10),
    (50, 50, 50, 50, 50, 50, 50, 50),
    (0, 0, 0, 0, 0, 0, 0, 0)
)

# The Middlegame and Endgame piece square tables are
WHITE_PAWN_MIDDLEGAME = (
    (0, 0, 0, 0, 0, 0, 0, 0),
    (5, 10, 12.5, -10, -10, 12.5, 10, 5),
    (0, 0, 5, 10, 10, 5, 0, 0),
    (0, 0, 5, 25, 25, 5, 0, 0),
    (5, 5, 10, 25, 25, 10, 5, 5),
    (0, 10, 10, 20, 20, 10, 10, 0),
    (50, 50, 50, -10, -10, 50, 50, 50),
    (0, 0, 0, 0, 0, 0, 0, 0)
)

WHITE_PAWN_ENDGAME = (
    (100, 100, 100, 100, 100, 100, 100, 100),
    (100, 100, 100, 100, 100, 100, 100, 100),
    (50, 50, 50, 50, 50, 50, 50, 50),
    (50, 50, 50, 50, 50, 50, 50, 50),
    (50, 50, 50, 50, 50, 50, 50, 50),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (-100, -100, -100, -100, -100, -100, -100, -100)
)

BLACK_PAWN_OPENING = reversed(WHITE_PAWN_OPENING)
BLACK_PAWN_MIDDLEGAME = reversed(WHITE_PAWN_MIDDLEGAME)
BLACK_PAWN_ENDGAME = reversed(WHITE_PAWN_ENDGAME)

WHITE_KNIGHT = (
    (-50, -40, -30, -30, -30, -30, -40, -50),
    (-40, -20, 0, 5, 5, 0, -20, -40),
    (-30, 5, 10, 15, 15, 10, 5, -30),
    (-30, 0, 15, 20, 20, 15, 0, -30),
    (-30, 5, 15, 20, 20, 15, 5, -30),
    (-30, 0, 10, 15, 15, 10, 0, -30),
    (-40, -20, 0, 0, 0, 0, -20, -40),
    (-50, -40, -30, -30, -30, -30, -40, -50)
)

BLACK_KNIGHT = reversed(WHITE_KNIGHT)

WHITE_BISHOP = (
    (-20, -10, -10, -10, -10, -10, -10, -20),
    (-10, 5, 0, 0, 0, 0, 5, -10),
    (-10, 10, 10, 10, 10, 10, 10, -10),
    (10, 0, 10, 10, 10, 10, 0, -10),
    (10, 5, 5, 10, 10, 5, 5, -10),
    (-10, 0, 5, 10, 10, 5, 0, -10),
    (-10, 0, 0, 0, 0, 0, 0, -10),
    (-20, -10, -10, -10, -10, -10, -10, -20)
)

BLACK_BISHOP = reversed(WHITE_BISHOP)
