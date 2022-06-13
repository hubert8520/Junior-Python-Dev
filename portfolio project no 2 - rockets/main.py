from classes_Rockets import RocketBoard

# show actual position of all of rockets
board = RocketBoard()

distance = RocketBoard.get_distance_between_rockets(board[0], board[2])
print(distance)
