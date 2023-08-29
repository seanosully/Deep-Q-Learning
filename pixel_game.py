import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
    STILL = 0
    RIGHT = 1
    LEFT = 2

# rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

FOOD_SIZE = 10
FALL_SPEED = 6
BUCKET_SPEED = 5
SPEED = 50

Pixel = namedtuple('Pixel', ['x', 'y'])

class PixelGameAI:

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Pixel Catch')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = Direction.STILL

        self.bucket_width = 50
        self.bucket_height = 20
        self.bucket_x = (self.w - self.bucket_width) // 2
        self.bucket_y = self.h - self.bucket_height

        self.score = 0
        self.falling_pixel = Pixel(random.randint(5, self.w - 5), -FOOD_SIZE)
        self.frame_iteration = 0

    def update_ui(self):
        self.display.fill(WHITE)

        # Draw the bucket
        pygame.draw.rect(self.display, BLACK, (self.bucket_x, self.bucket_y, self.bucket_width, self.bucket_height))

        # Draw the falling pixel
        pygame.draw.rect(self.display, RED, (self.falling_pixel.x, self.falling_pixel.y, FOOD_SIZE, FOOD_SIZE))

        text = font.render("Score: " + str(self.score), True, RED)
        self.display.blit(text, (10, 10))  # Display the score on the screen
        pygame.display.update()

    def move(self, action):
        if np.array_equal(action, [1, 0, 0]):
            self.bucket_x -= self.bucket_width

        elif np.array_equal(action, [0, 1, 0]):
            self.bucket_x += self.bucket_width

        elif np.array_equal(action, [0, 0, 0]):
            self.bucket_x = 0

        

        # Keep the bucket within the screen boundaries
        self.bucket_x = max(0, min(self.bucket_x, self.w - self.bucket_width))

    def play_step(self, action):
        self.frame_iteration += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        self.move(action)

        reward = 0
        game_over = False

      #  if self.frame_iteration > 400 * (self.score + 1):
       #     game_over = True
        #    reward = -10

        self.falling_pixel = Pixel(self.falling_pixel.x, self.falling_pixel.y + FALL_SPEED)

        if self.falling_pixel.y >= self.h:
            game_over = True
            reward = -10
            self.falling_pixel = Pixel(random.randint(1, 5) * self.w // 5 - 5, -FOOD_SIZE)


        if self.falling_pixel.x > self.bucket_x and self.falling_pixel.x < self.bucket_x + self.bucket_width:
            if self.bucket_y <= self.falling_pixel.y:
                self.falling_pixel = Pixel(random.randint(5, self.w - 5), -FOOD_SIZE)
                self.score += 1
            reward = 10
        print(reward)

        self.update_ui()
        self.clock.tick(SPEED)

        return reward, game_over, self.score


if __name__ == "__main__":
    game = PixelGameAI()
    game.run()
