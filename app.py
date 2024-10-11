import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Define colors
BACKGROUND_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BACKGROUND_COLOR)

# Board setup
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Drawing the grid
def draw_grid():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (SCREEN_WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

# Draw X or O
def draw_figure():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), 
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, 
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

# Check if there's a winner
def check_winner(player):
    # Vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Diagonal win check
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True

    return False

# Check if the board is full (for a tie)
def is_board_full():
    for row in board:
        if None in row:
            return False
    return True

# Restart the game
def restart():
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None

# Main game loop
draw_grid()
player = 'X'
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x coordinate
            mouseY = event.pos[1]  # y coordinate

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            # Place X or O on the board if the square is empty
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                draw_figure()

                # Check if the current player wins
                if check_winner(player):
                    game_over = True
                    print(f"{player} wins!")

                # Check if the board is full (tie)
                elif is_board_full():
                    game_over = True
                    print("It's a tie!")

                # Switch turns
                player = 'O' if player == 'X' else 'X'

        # Restart the game if spacebar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                restart()
                game_over = False
                player = 'X'

    pygame.display.update()
