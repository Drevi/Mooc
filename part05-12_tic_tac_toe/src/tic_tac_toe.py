# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or x > 2 or y < 0 or y > 2 or game_board[y][x]:
        return False
    game_board[y][x] = piece
    return True



