import chess
import random

board = chess.Board()

moves = list(board.legal_moves)
print(moves)
move = random.choice(moves)
print(move)
board.push(move)
print(board)
