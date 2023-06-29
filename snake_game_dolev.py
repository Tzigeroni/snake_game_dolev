import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def display(self):
        print('#' * (self.width + 2))

        for row in self.board:
            print('*', end= '')
            for cell in row:
                print(cell, end='')
            print('*', end='')
            print()

        print('#' * (self.width + 2))


class Snake:
    def __init__(self, board, head_segment='0', body_segment='o'):
        self.board = board
        self.head_segment = head_segment
        self.body_segment = body_segment
        self.position = self.spawn()
        self.direction = self.generate_direction()

    def spawn(self):
        x = random.randint(0, self.board.width - 1)
        y = random.randint(0, self.board.height - 1)
        return (x, y)

    def generate_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return random.choice(directions)

board = Board(30, 7)
snake = Snake(board)
snake.position = snake.spawn()
snake.direction = snake.generate_direction()


board.display()







