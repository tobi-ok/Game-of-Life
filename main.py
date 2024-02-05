import random
import time

life_probability = 30
game_width = 10
game_height = 10

class game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.last_state = None
        self.dead_state_count = 0

        self.live_cell = ' 🟦 '
        self.dead_cell = ' ⬜ '

        # Start with random board and render
        self.current_state = self.random_state()
        self.render()

    # Generate random board
    def random_state(self):
        board = [[0 if random.random() >= (life_probability/100) else 1 for _ in range(self.height)] for _ in range(self.width)]

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
            return self.current_state[x][y]
        except IndexError:
            return
    
    def next_board_state(self):
        self.last_state = [[y for y in x] for x in self.current_state]

        for x in range(self.width):
            for y in range(self.height):

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
                    self.current_state[x][y] = 0
                elif n_count == 3:
                    self.current_state[x][y] = 1
                    
        self.render()

    def render(self):
        matrix = self.current_state
        game_map = ''

        for x in range(self.width):
            for y in range(self.height):
                if matrix[x][y] == 1:
                    game_map += self.live_cell
                else:
                    game_map += self.dead_cell
                
            game_map += '\n'

        print(game_map)

if __name__ == '__main__':
    gol = game(game_width, game_height)

    while not gol.check_state():
        gol.next_board_state()
        time.sleep(0.1)

    print('Game over!')