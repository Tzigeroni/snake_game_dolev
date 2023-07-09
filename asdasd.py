import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def display(self):
        print('#' * (self.width + 2))
        for row in self.board:
            print('*', end='')
            for cell in row:
                print(cell, end='')
            print('*', end='')
        print('\n' + '#' * (self.width + 2))


class Snake:
    def __init__(self, head_segment='0', body_segment='o'):
        self.head_segment = head_segment
        self.body_segment = body_segment
        self.body_parts = []

    def move(self, direction):
        # Update the position of the snake's head based on the given direction
        head_x, head_y = self.body_parts[0]
        if direction == 'up':
            head_y -= 1
        elif direction == 'down':
            head_y += 1
        elif direction == 'left':
            head_x -= 1
        elif direction == 'right':
            head_x += 1
        self.body_parts.insert(0, (head_x, head_y))

    def update_body_parts(self):
        # Update the positions of the snake's body parts
        for i in range(1, len(self.body_parts)):
            self.body_parts[i] = self.body_parts[i-1]

class GameManager:
    def __init__(self, width, height):
        self.board = Board(width, height)
        self.snake = Snake()
        self.spawn_snake()

    def spawn_snake(self):
        x = random.randint(0, self.board.width - 1)
        y = random.randint(0, self.board.height - 3)  # Adjusted to leave space for 3 body parts
        self.snake.body_parts = [(x, y), (x, y+1), (x, y+2)]

    def display_board(self):
        self.board.board = [[' ' for _ in range(self.board.width)] for _ in range(self.board.height)]
        for body_part in self.snake.body_parts:
            x, y = body_part
            self.board.board[y][x] = self.snake.body_segment
        head_x, head_y = self.snake.body_parts[0]
        self.board.board[head_y][head_x] = self.snake.head_segment
        self.board.display()


game_manager = GameManager(30, 7)
game_manager.display_board()