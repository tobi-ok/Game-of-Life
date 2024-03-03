import random
import time
import os

life_probability = 30
game_width = 10
game_height = 10

class game:
    def __init__(self, width=game_width, height=game_height):
        self.width = width
        self.height = height
        self.last_state = None
        self.dead_state_count = 0

        self.live_cell = ' # '
        self.dead_cell = ' - '

        # Start with random board and render
        self.current_state = self.random_state()

    # Load state by file
    def load_board_state(self, filepath=None):
        filepath = filepath or input("Input filepath: ")
        last_state = self.current_state.copy()

        if os.path.exists(filepath):
            with open(filepath) as file:
                try:
                    for y, line in enumerate(file):
                        for x, cell in enumerate(line.strip()):
                            self.current_state[y][x] = int(cell)
                except:
                    print('Error - Failed to load board')
                    self.current_state = last_state

    # Generate random board
    def random_state(self):
        board = [[0 if random.random() >= (life_probability/100) else 1 for _ in range(self.width)] for _ in range(self.height)]

        return board
    
    # Check if board freezes
    def check_state(self):
        if self.current_state == self.last_state:
            self.dead_state_count += 1
        else:
            self.dead_state_count = 0

        if self.dead_state_count >= 5:
            return True
    
    def get_cell(self, x, y):
        if not self.current_state:
            return
        
        if (x < 0 or y < 0) or (x > self.width or y > self.height):
            return
        
        try:
            return self.current_state[y][x]
        except IndexError:
            return
    
    def next_board_state(self):
        self.last_state = [[x for x in y] for y in self.current_state]

        for y in range(self.height):
            for x in range(self.width):

                # Get cell's neighbors
                n = [
                    # ↖ ↑ ↗
                    self.get_cell(x-1, y-1),
                    self.get_cell(x, y-1),
                    self.get_cell(x+1, y-1),

                    # ←   →
                    self.get_cell(x-1, y),
                    self.get_cell(x+1, y),

                    # ↙ ↓ ↘
                    self.get_cell(x-1, y+1),
                    self.get_cell(x, y+1),
                    self.get_cell(x+1, y+1),
                ]
                n_count = 0

                # Count living neighbors
                for i in n:
                    if i is not None and i != 0:
                        n_count += 1
                
                # Determine cell's fate
                if n_count <= 1 or n_count > 3:
                    self.current_state[y][x] = 0
                elif n_count == 3:
                    self.current_state[y][x] = 1
                    
        self.render()

    def render(self):
        matrix = self.current_state
        game_map = ''

        for line in matrix:
            for cell in line:
                if cell == 1:
                    game_map += self.live_cell
                else:
                    game_map += self.dead_cell
                
            game_map += '\n'

        print(game_map)

    def run(self):
        print("Starting state: ")
        self.render()

        while not self.check_state():
            self.next_board_state()
            time.sleep(0.1)

if __name__ == '__main__':
    gol = game(game_width, game_height)
    gol.run()    
    print('Game over!')