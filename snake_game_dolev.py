import random
import pygame
import sys
import time
import os
import keyboard


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('#' * (self.width + 2))

        for row in self.board:
            print('*', end='')
            for cell in row:
                print(cell, end='')
            print('*', end='')
            print()

        print('#' * (self.width + 2))


class Snake:
    def __init__(self, head_segment='0', body_segment='o'):
        self.head_segment = head_segment
        self.body_segment = body_segment
        self.segments = [(0, 0)]
        self.direction = 'up'

    def move(self):
        head_x, head_y = self.segments[0]

        if self.direction == 'up':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'down':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'left':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'right':
            new_head = (head_x + 1, head_y)

        self.segments.insert(0, new_head)

    def change_direction(self, direction):
        if direction in ['up', 'down', 'left', 'right']:
            self.direction = direction


class GameManager:
    def __init__(self, width, height, refresh_rate=0.5):
        self.board = Board(width, height)
        self.snake = Snake()
        self.refresh_rate = refresh_rate

    def spawn_snake(self):
        x = random.randint(0, self.board.width - 1)
        y = random.randint(0, self.board.height - 1)
        self.snake.segments[0] = (x, y)
        self.board.board[y][x] = self.snake.head_segment

    def move_snake(self):
        self.snake.move()

    def change_snake_direction(self, direction):
        self.snake.change_direction(direction)

    def update_board(self):
        for segment in self.snake.segments[1:]:
            x, y = segment
            self.board.board[y][x] = ' '
        head_x, head_y = self.snake.segments[0]
        self.board.board[head_y][head_x] = self.snake.head_segment

    def handle_events(self):
        if keyboard.is_pressed('up'):
            self.change_snake_direction('up')
        elif keyboard.is_pressed('down'):
            self.change_snake_direction('down')
        elif keyboard.is_pressed('left'):
            self.change_snake_direction('left')
        elif keyboard.is_pressed('right'):
            self.change_snake_direction('right')


    def display_board(self):
        self.board.display()

    def run_game(self):
        self.spawn_snake()
        while True:
            self.handle_events()
            self.move_snake()
            self.update_board()
            self.display_board()
            time.sleep(self.refresh_rate)



game_manager = GameManager(30, 10, refresh_rate=0.0004)
game_manager.run_game()
