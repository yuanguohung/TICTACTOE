import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define game variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
player_turn = 'X'
game_over = False

# Define menu variables
def draw_menu():
    window.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render("Tic Tac Toe", True, BLACK)
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
    window.blit(text, text_rect)
    #click the button to start the game
    font = pygame.font.Font(None, 36)
    text = font.render("Click to start", True, BLACK)
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2 + 50))
    window.blit(text, text_rect)
    

def draw_board():
    window.fill(WHITE)
    pygame.draw.line(window, BLACK, (window_width/3, 0), (window_width/3, window_height), 5)
    pygame.draw.line(window, BLACK, (2*window_width/3, 0), (2*window_width/3, window_height), 5)
    pygame.draw.line(window, BLACK, (0, window_height/3), (window_width, window_height/3), 5)
    pygame.draw.line(window, BLACK, (0, 2*window_height/3), (window_width, 2*window_height/3), 5)
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                pygame.draw.line(window, BLACK, (j*window_width/3 + 20, i*window_height/3 + 20), ((j+1)*window_width/3 - 20, (i+1)*window_height/3 - 20), 5)
                pygame.draw.line(window, BLACK, ((j+1)*window_width/3 - 20, i*window_height/3 + 20), (j*window_width/3 + 20, (i+1)*window_height/3 - 20), 5)
            elif board[i][j] == 'O':
                pygame.draw.circle(window, BLACK, (int((j+0.5)*window_width/3), int((i+0.5)*window_height/3)), int(window_width/6 - 20), 5)

def is_game_over():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != '':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True
    # Check if the board is full
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                return False
    return True

computer = 'O'  # Declare and assign a value to the "computer" variable
def make_computer_move():
    # Check if the board is full
    if is_game_over():
        return
    
    # Check if the computer can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = computer
                if is_game_over():
                    return
                board[i][j] = ''
                
    # Check if the player can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = player_turn
                if is_game_over():
                    board[i][j] = computer
                    return
                board[i][j] = ''

    # Generate random moves until an empty cell is found
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == '':
            board[i][j] = computer
            break

# Main game loop

# Define the menu state

menu = True
game = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu:
                menu = False
                game = True
            elif game:
                x, y = pygame.mouse.get_pos()
                i = y // (window_height // 3)
                j = x // (window_width // 3)
                if board[i][j] == '' and not game_over:
                    board[i][j] = player_turn
                    if is_game_over():
                        game_over = True
                    else:
                        make_computer_move()
                        if is_game_over():
                            game_over = True

    if menu:
        draw_menu()
    elif game:
        draw_board()
        if game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, RED)
            text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
            window.blit(text, text_rect)

    pygame.display.update()
    pygame.time.Clock().tick(30)
    
    if is_game_over():
    # if gameover quit the game after 1 second
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()
    



