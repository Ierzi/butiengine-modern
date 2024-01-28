# ButiEngine Modern by Ierzi.
# A chess engine I made for fun, trying to keep the code as simple and documented as possible.
# This is the modern version of my very first chess engine, ButiEngine, which didn't work. :(
# --------------------------------------------------------------------------------------
# The creation started on January 23rd, 2024. There weren't much, just the main class (which was empty)
# I really started creating it one day later, it came with the king square table and the main class.
# Go see the commits history on the GitHub repository to know to full timeline.
# -------------------------------------------------------------------------------------
# Useful links: https://www.chessprogramming.org, https://github.com/Ierzi/butiengine-modern/wiki

import chess
import os
import sys
import rich
import piecesquaretables as pst

# Checking for the minimum supported version to use
if not sys.version_info.major <= 3 or sys.version_info.minor < 5:
    print("You are using an outdated version of Python.")
    print("Please download the new version of Python at python.org")


# The main class of the engine
class ButiEngine:
    def __init__(self):
        """The modern version of my chess engine."""
        # Older private versions used a variable for the piece square tables
        # Now, this is moved to the piecesquaretables/ folder.

    def evaluate(self, board: list[list[str]]):
        pass
        # best_evaluation = float("-inf")

    def search(self, board: list[list[str]], depth: int = 3):
        pass

    def _search_min(self, board: chess.Board, depth: int, alpha: int, beta: int):

        if depth == 0:
            return -self.evaluate()

        for move in board.legal_moves:
            board.push(move)
            score = self._search_max(board, depth - 1, alpha, beta)
            board.pop()

            if score <= alpha:
                return alpha
            if score < beta:
                beta = score

        return beta

    def _search_max(self, board: chess.Board, depth: int, alpha: int, beta: int):

        if depth == 0:
            return self.evaluate()

        for move in board.legal_moves:
            board.push(move)
            score = self._search_min(board, depth - 1, -alpha, -beta)
            board.pop()

            if score <= alpha:
                return alpha
            if score < beta:
                beta = score

        return beta

    @staticmethod
    def board_to_fen(self, board: list[list[str]]) -> str:
        # The board to fen code is "stolen" from the original ButiEngine, which I used in MixusEngine too.
        # It works, and that's the essential. Probably not the most efficient way neither!

        fen_voids = 0
        is_not_first_time = False
        fen = ""
        for rank in range(8):

            if is_not_first_time:
                fen += "/"
            else:
                is_not_first_time = True

            for file in range(8):
                _piece = board[rank][file]
                if _piece == ".":
                    fen_voids += 1
                    if fen_voids == 8:
                        fen_voids = 0
                        fen += f"8"
                    elif file == 7:  # End of the line
                        fen += f"{fen_voids}"
                        fen_voids = 0

                elif _piece == "P":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "P"
                elif _piece == "p":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "p"
                elif _piece == "N":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "N"
                elif _piece == "n":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "n"
                elif _piece == "B":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "B"
                elif _piece == "b":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "b"
                elif _piece == "R":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "R"
                elif _piece == "r":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "r"
                elif _piece == "Q":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "Q"
                elif _piece == "q":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "q"
                elif _piece == "K":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "K"
                elif _piece == "k":
                    if fen_voids != 0:
                        fen += f"{fen_voids}"
                        fen_voids = 0
                    fen += "k"

        return self.fen


if __name__ == "__main__":
    buti = ButiEngine()
