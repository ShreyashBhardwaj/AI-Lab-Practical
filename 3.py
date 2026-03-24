# Simulate the Wumpus World using rule-based logic to show how decisions are made with uncertainty.
import random
class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        self.agent_position = (0, 0)
        self.gold_position = None
        self.wumpus_position = None
        self.pit_positions = set()
        self.visited = set()
        self.visited.add(self.agent_position)
        self._place_items()
    def _place_items(self):
        # Place Gold, Wumpus, and Pits randomly, ensuring they are not at (0,0)
        self.gold_position = self._get_random_empty_cell()
        self.grid[self.gold_position[0]][self.gold_position[1]] = 'G'
        self.wumpus_position = self._get_random_empty_cell()
        self.grid[self.wumpus_position[0]][self.wumpus_position[1]] = 'W'
        self._add_percept_marker(self.wumpus_position, 'S') # Stench
        num_pits = random.randint(1, 3) # Example: 1 to 3 pits
        for _ in range(num_pits):
            pit_pos = self._get_random_empty_cell()
            self.pit_positions.add(pit_pos)
            self.grid[pit_pos[0]][pit_pos[1]] = 'P'
            self._add_percept_marker(pit_pos, 'B') # Breeze
    def _get_random_empty_cell(self):
        while True:
            r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (r, c) != (0, 0) and self.grid[r][c] == '.':
                return (r, c)
    def _add_percept_marker(self, pos, marker):
        r, c = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # Adjacent cells
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size and self.grid[nr][nc] == '.':
                self.grid[nr][nc] = marker
    def display_world(self):
        for r_idx, row in enumerate(self.grid):
            display_row = []
            for c_idx, cell in enumerate(row):
                if (r_idx, c_idx) == self.agent_position:
                    display_row.append('A')
                else:
                    display_row.append(cell if cell else '.')
            print(' | '.join(display_row))
        print("\n")
    def get_percepts(self):
        r, c = self.agent_position
        percepts = []
        if (r, c) == self.gold_position:
            percepts.append("Glitter")
        if (r, c) == self.wumpus_position:
            percepts.append("Wumpus!")
        if (r, c) in self.pit_positions:
            percepts.append("Pit!")
        # Check for adjacent stench and breeze
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                if (nr, nc) == self.wumpus_position and "Stench" not in percepts:
                    percepts.append("Stench")
                if (nr, nc) in self.pit_positions and "Breeze" not in percepts:
                    percepts.append("Breeze")
        return percepts
    def move_agent(self, direction):
        x, y = self.agent_position
        new_x, new_y = x, y
        if direction == 'U': new_x -= 1
        elif direction == 'D': new_x += 1
        elif direction == 'L': new_y -= 1
        elif direction == 'R': new_y += 1
        else:
            print("Invalid move!")
            return False
        if 0 <= new_x < self.size and 0 <= new_y < self.size:
            self.agent_position = (new_x, new_y)
            self.visited.add(self.agent_position)
            return True
        else:
            print("Cannot move out of bounds!")
            return False
# Example Usage
if __name__ == "__main__":
    game = WumpusWorld()
    print("Initial Wumpus World:")
    game.display_world()
    while True:
        percepts = game.get_percepts()
        print(f"Current Percepts: {percepts}")
        if "Wumpus!" in percepts or "Pit!" in percepts:
            print("Game Over! You died.")
            break
        if "Glitter" in percepts:
            print("You found the Gold! You win!")
            break
        move = input("Enter move (U/D/L/R): ").upper()
        if not game.move_agent(move):
            print("Try again.")
        game.display_world()