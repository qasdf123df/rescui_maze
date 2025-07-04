import API
import sys
from collections import deque
# отсчет с 0
# n - right
# e - 
# s - 
# w - down
def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()
def explore_maze_dfs(x=0, y=0, current_dir=0):
    visited = set()
    log("start dfs")
    visited.add((x, y))
    
    if not API.wallFront():
        new_x, new_y = get_new_position(x, y, current_dir)
        if (new_x, new_y) not in visited:
            API.moveForward()
            log(f"new: ({new_x}, {new_y})")
            API.setColor(new_x, new_y, 'g')
            
            explore_maze_dfs(new_x, new_y, current_dir)
            
            API.turnRight()
            API.turnRight()
            API.moveForward()
            API.turnRight()
            API.turnRight()
    if not API.wallRight():
        new_x, new_y = get_new_position(x, y, (current_dir + 1) % 4)
        if (new_x, new_y) not in visited:
            API.turnRight()
            API.moveForward()
            log(f"new: ({new_x}, {new_y})")
            API.setColor(new_x, new_y, 'g')
            
            explore_maze_dfs(new_x, new_y, (current_dir + 1) % 4)
            
            API.turnRight()
            API.turnRight()
            API.moveForward()
            API.turnRight()
    if not API.wallLeft():
        new_x, new_y = get_new_position(x, y, (current_dir - 1) % 4)
        if (new_x, new_y) not in visited:
            API.turnLeft()
            API.moveForward()
            log(f"new: ({new_x}, {new_y})")
            API.setColor(new_x, new_y, 'g')
            
            explore_maze_dfs(new_x, new_y, (current_dir - 1) % 4)
            
            API.turnLeft()
            API.turnLeft()
            API.moveForward()
            API.turnLeft()
            
    log("all")

def get_new_position(x, y, dir):
    if dir == 0:    
        return (x, y + 1)
    elif dir == 1:   
        return (x + 1, y)
    elif dir == 2:   
        return (x, y - 1)
    elif dir == 3:   
        return (x - 1, y)

# def explore_maze_dfs():
#     log("start dfs")
#     x, y = 0, 0
    
#     visited = set()
#     visited.add((x, y))
    
#     stack = []
#     stack.append((x, y, 0))
    
#     while stack:
#         x, y, current_dir = stack[-1] 
#         moved = False
#         for _ in range(4):
#             if not API.wallFront():
#                 new_x, new_y = get_new_position(x, y, current_dir)
#                 if (new_x, new_y) not in visited:
#                     API.moveForward()
#                     x, y = new_x, new_y
#                     visited.add((x, y))
#                     stack.append((x, y, current_dir))
#                     log(f"new: ({x}, {y})")
#                     API.setColor(x,y,'g')
#                     moved = True
#                     break
            
#             # elif not API.wallRight():
#             #     API.turnRight()
#             # elif not API.wallRight():
#             API.turnRight()
#             current_dir = (current_dir + 1) % 4
#             # elif not API.wallLeft():
#             #     current_dir = (current_dir - 1) % 4
#             #     API.turnLeft()
#             # else:
#             #     API.turnLeft()
#             #     API.turnLeft()+

#             #     current_dir = (current_dir + 2) % 4

        
#         if not moved:
#             if len(stack) > 1:  
#                 API.turnRight()
#                 API.turnRight()
#                 current_dir = (current_dir + 2) % 4
#                 API.moveForward()
#                 x, y = get_new_position(x, y, current_dir)
#                 stack.pop()
#                 prev_x, prev_y, prev_dir = stack[-1]
#                 while current_dir != prev_dir:
#                     API.turnRight()
#                     current_dir = (current_dir + 1) % 4
#             else:
#                 break  # всё исследовано
    
#     log("all")


def main():
    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "start")
    # while not API.wallFront():
    #     # if not API.wallLeft():
    #     #     API.turnLeft()
    #     # while API.wallFront():
    #     #     API.turnRight()
    #     API.moveForward()
    # log("start bfs")
    # explore_maze_bfs()
    explore_maze_dfs()

if __name__ == "__main__":
    main()
