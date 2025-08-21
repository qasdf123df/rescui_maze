import API
import sys
from collections import deque
UNVISITED = 0
VISITED_ONCE = 1
VISITED_TWICE = 2

class TremauxSolver:
    def __init__(self):
        self.x, self.y = 0, 0
        self.direction = 0  # 0: вверх, 1: право, 2: низ, 3: лево
        
        # Словарь для отслеживания состояния проходов между клетками
        # Ключ: ((x1, y1), (x2, y2)) - координаты двух соседних клеток
        # Значение: состояние прохода
        self.passages = {}
        
        # Множество посещенных клеток
        self.visited_cells = set()
        self.visited_cells.add((0, 0))
        
        self.backtrack_stack = []

    def get_current_cell(self):
        return (self.x, self.y)

    def get_neighbor_cell(self, direction_offset):
        new_direction = (self.direction + direction_offset) % 4
        
        if new_direction == 0:
            return (self.x, self.y + 1)
        elif new_direction == 1:
            return (self.x + 1, self.y)
        elif new_direction == 2:
            return (self.x, self.y - 1)
        else:
            return (self.x - 1, self.y)

    def get_passage_key(self, cell1, cell2):
        return tuple(sorted([cell1, cell2]))

    def check_wall(self, direction_offset):
        if direction_offset == 0:
            return API.wallFront()
        elif direction_offset == 1:  
            return API.wallRight()
        elif direction_offset == -1:  
            return API.wallLeft()
        return True

    def turn_to(self, target_direction):
        turn = self.direction - target_direction
        print(turn)
        if turn == 3:
            API.turnRight()
            self.direction = (self.direction + 1) % 4
        elif turn == -3:
            API.turnLeft()
            self.direction = (self.direction - 1) % 4

        elif turn == 2 or turn == -2:
            API.turnRight()
            API.turnRight()
            self.direction = (self.direction + 2) % 4
        elif turn < 0:
            API.turnRight()
            self.direction = (self.direction + 1) % 4
        elif turn > 0 :
            API.turnLeft()
            self.direction = (self.direction - 1) % 4

        # while self.direction != target_direction:

    def move_to(self, target_cell):

        dx = target_cell[0] - self.x
        dy = target_cell[1] - self.y
        
        if dy == 1:
            target_direction = 0
        elif dx == 1:
            target_direction = 1
        elif dy == -1:
            target_direction = 2
        else:
            target_direction = 3
            
        self.turn_to(target_direction)
        API.moveForward()
        
        
        self.x, self.y = target_cell
        self.visited_cells.add((self.x, self.y))

    def get_available_directions(self):
        available = []
        for direction_offset in [0, 1, -1]:
            if not self.check_wall(direction_offset):
                neighbor = self.get_neighbor_cell(direction_offset)
                passage_key = self.get_passage_key(self.get_current_cell(), neighbor)
                
                if passage_key not in self.passages or self.passages[passage_key] != VISITED_TWICE:
                    available.append((direction_offset, neighbor))
        
        return available

    def explore(self):        
        while True:
            current_cell = self.get_current_cell()
            print(f"curr poz: {current_cell}")
            
            available_dirs = self.get_available_directions()
            
            if not available_dirs:
                if not self.backtrack_stack:
                    print("ne posos")
                    break

                prev_cell = self.backtrack_stack.pop()
                passage_key = self.get_passage_key(current_cell, prev_cell)
                self.passages[passage_key] = VISITED_TWICE
                
                print(f"Backtracking to {prev_cell}")
                self.move_to(prev_cell)
                continue
            
            direction_offset, next_cell = available_dirs[0]
            
            passage_key = self.get_passage_key(current_cell, next_cell)
            if passage_key not in self.passages:
                self.passages[passage_key] = VISITED_ONCE
            else:
                self.passages[passage_key] = VISITED_TWICE
            
            self.backtrack_stack.append(current_cell)
            
            self.turn_to((self.direction + direction_offset) % 4)
            API.setColor(self.x, self.y, 'g')
            API.moveForward()
            self.x, self.y = next_cell
            self.visited_cells.add(next_cell)
            
            print(f"Moving to {next_cell}")

    def get_shortest_path_home(self):
        from collections import deque
        
        graph = {}
        for passage, state in self.passages.items():
            if state != VISITED_TWICE:
                cell1, cell2 = passage
                if cell1 not in graph:
                    graph[cell1] = []
                if cell2 not in graph:
                    graph[cell2] = []
                graph[cell1].append(cell2)
                graph[cell2].append(cell1)
                
        queue = deque([(self.get_current_cell(), [])])
        visited = set()
        
        while queue:
            current, path = queue.popleft()
            
            if current == (0, 0):
                return path + [current]
            
            if current in visited:
                continue
                
            visited.add(current)
            
            for neighbor in graph.get(current, []):
                queue.append((neighbor, path + [current]))
        
        return None

    def return_home(self):
        print("I always come back...")
        
        path = self.get_shortest_path_home()
        if not path:
            print("posos nahuy")
            return
        
        print(f"best {path}")
        
        for i in range(1, len(path)):
            self.move_to(path[i])
            print(f"go to {path[i]}")

if __name__ == "__main__":
    solver = TremauxSolver()
    
    try:
        solver.explore()
        solver.return_home()
        
        print("thaths all!")
        
    except Exception as e:
        print(f"total err: {e}")
