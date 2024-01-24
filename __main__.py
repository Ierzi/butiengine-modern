import chess
import os
import sys
import rich
from rich import print as rprint
import piecesquaretables as pst

if not sys.version_info.major >= 3:
    print("You are using an outdated version of Python.")
    print("Please download the new version of Python at python.org")


# ButiEngine Modern by Ierzi.
# A chess engine I made for fun, trying to keep the code as simple and documented as possible.
# This is the modern version of my very first chess engine, ButiEngine, which didn't work. :(
# --------------------------------------------------------------------------------------
# The creation started on January 23rd, 2024. There weren't much, just the main class (which was empty)
# I really started creating it one day later, it came with the king square table and the main class.
# Go see the commits history on the GitHub repository to know to full timeline.

# The main class of the engine
class ButiEngine:
    def __init__(self):
        """The modern version of my chess engine."""
        # Older private versions used a variable for the piece square tables
        # Now, this is moved to the piecesquaretables/ folder.

    def evaluate(self, board: list[list[str]]):
        evaluation = 0
        fen = self.board_to_fen(board)

    def best_move(self):
        pass

    @staticmethod
    def board_to_fen(self, board: list[list[str]]) -> str:
        # The board to fen code is "stolen" from the original ButiEngine, which I used in MixusEngine too.
        # It works, and that's the essential.
        pass


if __name__ == "__main__":
    buti = ButiEngine()
