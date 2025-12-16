import random
import pygame
import math


pygame.init()

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

def display_board(board):
    window_size = (600, 700)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Battleship")
    pygame.font.init()
    k = 0
    coord_1 = 0
    coord_2 = 101010

    running = True
    while running and k < len(ships) * 2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
            
                click_x, click_y = event.pos
                grid_x = (click_x - 20) // 55
                grid_y = (click_y - 100) // 55
                box_x = 20 + grid_x * 55
                box_y = 100 + grid_y * 55
                coord_1 = (grid_x, grid_y) if k % 2 == 0 else coord_1
                coord_2 = (grid_x, grid_y) if k % 2 == 1 else coord_2 
                if k % 2 == 1:
                    for i in range(ships_sizes[ships[k // 2]]):
                        if coord_1[0] == coord_2[0]:  # vertical
                            y_pos = coord_1[1] + i if coord_2[1] > coord_1[1] else coord_1[1] - i
                            board_player[y_pos][coord_1[0]] = 1
                        else:  # horizontal
                            x_pos = coord_1[0] + i if coord_2[0] > coord_1[0] else coord_1[0] - i
                            board_player[coord_1[1]][x_pos] = 1
                board_player[grid_y][grid_x] = 1
                pygame.draw.rect(window, (0, 0, 0) , (box_x, box_y, 50, 50), 5) 
                k += 1
        x_coord = 20
        y_coord = 100
        # Draw shapes
        window.fill((255, 255, 255))
        
        for row in board: 
            for i in range(len(row)):
                if row[i] == 0:
                    pygame.draw.rect(window, (0, 0, 0) , (x_coord, y_coord, 50, 50), 5)
                else:
                    pygame.draw.rect(window, (0, 0, 0) , (x_coord, y_coord, 50, 50))
                x_coord += 55
            y_coord += 55
            x_coord = 20
        font = pygame.font.SysFont('Arial', 25)
        print(k)
        if k >= len(ships) * 2:
            if k % 2 == 0:
                text_surface = font.render(f"Now Placing {ships[k // 2 ]}: Where Should Your Ship Start", False, (255,0,0))
            else:
                text_surface = font.render(f"Now Placing {ships[k // 2 ]}: Chose a Second Square to Decide Orientation", False, (255,0,0))
            window.blit(text_surface, (0, 20)) 



        pygame.display.flip()
    pygame.quit()

generate_board()
display_board(board_player)
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
    
