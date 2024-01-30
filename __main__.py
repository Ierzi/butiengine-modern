# ButiEngine Modern by Ierzi.
# A chess engine I made for fun, trying to keep the code as simple and documented as possible.
# This is the modern version of my very first chess engine, ButiEngine, which didn't work. :(
# --------------------------------------------------------------------------------------
# The creation started on January 23rd, 2024. There weren't much, just the main class (which was empty)
# I really started creating it one day later, it came with the king square table and the main class.
# Go see the commits history on the GitHub repository to know to full timeline.
# -------------------------------------------------------------------------------------
# Useful links: https://www.chessprogramming.org, https://github.com/Ierzi/butiengine-modern/wiki

from rich.console import Console
import chess
import os
import sys
import piecesquaretables as pst
from typing import Literal

console = Console()


# Checking for the minimum supported version to use
if not sys.version_info.major <= 3 or sys.version_info.minor < 5:
    console.print("[red]You're using an outdated version of Python. Please download the latest version at python.org")
    sys.exit(1)


# The main class of the engine
class ButiEngine:
    def __init__(self):
        """The modern version of my chess engine."""
        # Older private versions used a variable for the piece square tables
        # Now, this is moved to the piecesquaretables/ folder.

    def get_game_phase(self, board: list[list[str]]) -> Literal["OPENING", "MIDDLEGAME", "ENDGAME"]:
        pass

    def evaluate(self, board: list[list[str]]) -> int:
        score_list = []
        for index, row in enumerate(board):
            for index2, case in enumerate(row):
                score_list.append(pst.piecesquaretables_score(case, (index, index2), game_phase=self.get_game_phase()))

        return 0

    def search(self, board: list[list[str]], turn: bool, depth: int = 3):
        pass

    def _search_min(self, board: chess.Board, depth: int, alpha: int, beta: int) -> int:

        if depth == 0:
            _board = self.fen_to_board(board.fen())
            return -self.evaluate(_board)

        for move in board.legal_moves:
            board.push(move)
            score = self._search_max(board, depth - 1, alpha, beta)
            board.pop()

            if score <= alpha:
                return alpha
            if score < beta:
                beta = score

        return beta

    def _search_max(self, board: chess.Board, depth: int, alpha: int, beta: int) -> int:

        if depth == 0:
            _board = self.fen_to_board(board.fen())
            return self.evaluate(_board)

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
    def board_to_fen(board: list[list[str]]) -> str:
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

        return fen

    @staticmethod
    def fen_to_board(fen: str) -> list[list[str]]:
        board: list[list[str]]

        # Split the FEN string into separate components
        fen_parts = fen.split()
        fen_position = fen_parts[0]  # Position component of FEN

        # Convert FEN position string to nested list representation
        rank_strings = fen_position.split('/')

        for rank, rank_string in enumerate(rank_strings):
            file_index = 0

            for char in rank_string:
                if char.isdigit():
                    file_index += int(char)
                else:
                    piece = char
                    board[7 - rank][file_index] = piece
                    file_index += 1

        # Replace None with "."
        for rank in range(8):
            for file in range(8):
                if board[rank][file] is None:
                    board[rank][file] = "."

        return board


if __name__ == "__main__":
    buti = ButiEngine()
    print(chess.STARTING_FEN)
