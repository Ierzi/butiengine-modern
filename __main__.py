import chess
import os
import sys
import rich
from rich import print as rprint
import piecetables

if not sys.version_info.major >= 3:
    print("You are using an outdated version of Python.")
    print("Please download the new version of Python at python.org")


# ButiEngine Modern by Ierzi.
# A chess engine I made for fun, trying to keep the code as simple and documented as possible.
# This is the modern version of my very first chess engine, ButiEngine, which didn't work. :(
# --------------------------------------------------------------------------------------
# The creation started on January 22nd, 2024. There weren't much, just the main class (which was empty)
# I really started creating it two days later, it came with the king square table and the main class

# The main class of the engine
class ButiEngine:
    def __init__(self):
        """The modern version of my chess engine."""
        # Older private versions used a variable for the piece square tables
        # Now, this is moved to the piecetables/ folder.


if __name__ == "__main__":
    buti = ButiEngine()
