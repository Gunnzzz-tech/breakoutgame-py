import pygame
import sys
from bricks import Brick
from constants import BLACK, WHITE
from ball import Ball
from paddle import Paddle
from config import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()

# FPS and screen setup
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Font for text
font = pygame.font.Font(None, 50)

# Clock for controlling frame rate
clock = pygame.time.Clock()

def main():
    paddle = Paddle()
    ball = Ball()
    bricks = [Brick(x * 100, y * 30, 80, 20) for x in range(8) for y in range(5)]
    running = True
    game_over = False
    score = 0  # Initialize score

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Exit on mouse click if the game is over
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Game logic only runs if the game is not over
        if not game_over:
            keys = pygame.key.get_pressed()
            paddle.move(keys)
            ball.move()

            # Ball collision with the paddle
            if paddle.x <= ball.x <= paddle.x + paddle.width and paddle.y <= ball.y + ball.radius <= paddle.y + paddle.height:
                ball.speed_y = -ball.speed_y

            # Ball collision with bricks
            for brick in bricks:
                if brick.active and brick.rect.collidepoint(ball.x, ball.y):
                    ball.speed_y = -ball.speed_y
                    brick.active = False
                    score += 10  # Increment score for each brick hit

            # Ball falls below the paddle (game over)
            if ball.y > SCREEN_HEIGHT:
                game_over = True

        # Drawing on the screen
        screen.fill(BLACK)

        if game_over:
            # Display "Game Over" text
            game_over_text = font.render(f"Game Over! Your Score: {score}. Click to Exit.", True, WHITE)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(game_over_text, text_rect)
        else:
            # Draw paddle, ball, and bricks
            paddle.draw(screen)
            ball.draw(screen)
            for brick in bricks:
                brick.draw(screen)

            # Display the score at the top-left corner
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()

# Entry point of the script
if __name__ == '__main__':
    main()
