import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Guess That Number!")

White = (255, 255, 255)
Black = (0,0,0)
CadetBlue = (95,158,160)

number_to_guess = random.randint(1,100)

font = pygame.font.Font(None, 36)
def display_message(message):
    screen.fill(CadetBlue)
    text_surface = font.render(message, True, Black)
    text_rect = text_surface.get_rect(center=(200, 150))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def draw_text_input_box(rect, text):
    pygame.draw.rect(screen, White, rect, 2)
    text_surface = font.render(text, True, Black)
    screen.blit(text_surface, (rect.x + 5, rect.y + 5))

guess = ""
input_box_rect = pygame.Rect(100, 200, 200, 30)
running = True
while running:
    display_message("Guess the number (1-100):")

    draw_text_input_box(input_box_rect, guess)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if guess.isdigit():
                    guess_num = int(guess)
                    if guess_num == number_to_guess:
                        display_message("Congratulations! You guessed the number")
                        running = False
                    elif guess_num < number_to_guess:
                        display_message("Try guessing higher")
                    else:
                        display_message("Try guessing lower")
                    guess = ""
                else:
                    display_message("Please enter a valid number!")
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            elif event.key == pygame.K_ESCAPE:
                guess = ""
            else:
                guess += event.unicode

    pygame.display.flip()

pygame.quit()