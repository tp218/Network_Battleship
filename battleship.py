import random

rows = {
    "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9
}

row_keys = list(rows.keys())
ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

ships_sizes = {
    "Carrier" : 5,
    "Battleship" : 4,
    "Cruiser" : 3,
    "Submarine" : 3,
    "Destroyer" : 2
}

board_player = [
    [1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    
]

board_ai = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    
]

def generate_board():
    for ship in ships:
        size = ships_sizes[ship]
        starting_x = random.randint(0, 9)
        starting_y = random.randint(0, 9)
        orientation = random.choice(["horizontal", "vertical"])
        if are_colissions(size, starting_x, starting_y, board_ai, orientation):
            while are_colissions(size, starting_x, starting_y, board_ai, orientation):
                starting_x = random.randint(0, 9)
                starting_y = random.randint(0, 9)
                orientation = random.choice(["horizontal", "vertical"])
        if orientation == "horizontal":
            if starting_x + size <= 9:
                for i in range(size):
                    board_ai[starting_y][starting_x + i] = 1
            else:
                for i in range(size):
                    board_ai[starting_y][starting_x - i] = 1
        else:
            if starting_y + size <= 9:
                for i in range(size):
                    board_ai[starting_y + i][starting_x] = 1
            else:
                for i in range(size):
                    board_ai[starting_y - i][starting_x] = 1

def are_colissions(size, start_x, start_y, board, orientation):
    if orientation == "horizontal":
        for i in range(size):
            if(start_x + size <= 9):
                
                if board[start_y][start_x + i] == 1:
                    return True
                
            else: 
                if board[start_y][start_x - i] == 1:
                    return True
    else:
        for i in range(size):
            if(start_y + size <= 9):
                
                if board[start_y + i][start_x] == 1:
                    return True
                
            else: 
                if board[start_y - i][start_x] == 1:
                    return True
        else:
            return False

generate_board()
print(board_ai)

# spot = input("where would you like to hit")
# hit_spot = board_ai[rows[spot[0]]][int(spot[1]) - 1]
# if hit_spot == 1:
#     print("hit")
# else:
#     print("miss")

# hitspot_ai = board_player[rows[random.choice(row_keys)]][random.randint(0,9)]
# if hitspot_ai == 1:
#     print("AI hit your ship!")
# else:
#     print("AI missed!")
    
