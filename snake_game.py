import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
bg_color = (50, 153, 113,0)
wall_color = (60,70,80)
snake_color = (134,176,186)

# Display dimensions
display_width = 800
display_height = 600

# Create game window
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 15

# Wall dimensions
wall_thickness = 20
top_border_thickness = 40  # Increased border at the top

# Load pixel font
pixel_font = pygame.font.Font("PressStart2P.ttf", 25)  # Adjust size as needed

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    lines = msg.split('\n')
    line_height = pixel_font.get_height()
    total_height = len(lines) * line_height
    y = (display_height - total_height) / 2  # Start position to center vertically
    for line in lines:
        mesg = pixel_font.render(line, True, color)
        text_rect = mesg.get_rect(center=(display_width / 2, y))
        display.blit(mesg, text_rect)
        y += line_height  # Move to the next line

def draw_walls():
    pygame.draw.rect(display, wall_color, [0, 0, display_width, wall_thickness+20])  # Top border
    pygame.draw.rect(display, wall_color, [0, wall_thickness, wall_thickness, display_height - 2 * wall_thickness])
    pygame.draw.rect(display, wall_color, [0, display_height - wall_thickness, display_width, wall_thickness])
    pygame.draw.rect(display, wall_color, [display_width - wall_thickness, wall_thickness, wall_thickness, display_height - 2 * wall_thickness])

def show_score(score):
    high_score = load_high_score()
    score_text = pixel_font.render("Score: " + str(score), True, white)
    high_score_text = pixel_font.render("High Score: " + str(high_score), True, white)

    # Calculate positions for score and high score
    score_x = display_width / 4 - score_text.get_width() / 2
    high_score_x = 3 * display_width / 4 - high_score_text.get_width() / 2
    y = top_border_thickness / 2 - score_text.get_height() / 2

    # Blit score and high score onto the screen
    display.blit(score_text, [score_x, y])
    display.blit(high_score_text, [high_score_x, y])


def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        # Return 0 if high score file doesn't exist
        return 0

def update_high_score(score):
    current_high_score = load_high_score()
    if score > current_high_score:
        save_high_score(score)

def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(wall_thickness, display_width - wall_thickness - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(wall_thickness + top_border_thickness, display_height - wall_thickness - snake_block) / 10.0) * 10.0  # Adjusted position

    score = 0

    while not game_over:

        while game_close == True:
            display.fill(bg_color)
            message("You Lost!\nPress Q to Quit\nPress C to Play Again", white)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= display_width - wall_thickness or x1 < wall_thickness or y1 >= display_height - wall_thickness or y1 < top_border_thickness + wall_thickness:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(bg_color)
        draw_walls()
        show_score(score)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(wall_thickness, display_width - wall_thickness - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(wall_thickness + top_border_thickness, display_height - wall_thickness - snake_block) / 10.0) * 10.0  # Adjusted position
            length_of_snake += 1
            score += 1
            update_high_score(score)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

