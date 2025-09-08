from collections import deque

# Board size (3x3 puzzle)
N = 3

# Moves: Up, Down, Left, Right
moves = [(-1,0),(1,0),(0,-1),(0,1)]

# Helper: Find position of blank tile
def find_blank(state):
    idx = state.index("_")
    return divmod(idx, N)

# Helper: Swap tiles
def swap(state, i1, j1, i2, j2):
    s = list(state)
    idx1, idx2 = i1*N+j1, i2*N+j2
    s[idx1], s[idx2] = s[idx2], s[idx1]
    return tuple(s)

# Expand node: Generate next states
def expand(state):
    x, y = find_blank(state)
    children = []
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            children.append(swap(state, x, y, nx, ny))
    return children

# Depth Limited Search
def dls(state, goal, limit, path, visited):
    if state == goal:
        return path
    
    if limit == 0:
        return None
    
    visited.add(state)
    for child in expand(state):
        if child not in visited:
            result = dls(child, goal, limit-1, path+[child], visited)
            if result is not None:
                return result
    visited.remove(state)
    return None

def iddfs(start, goal, max_depth=20):
    for depth in range(max_depth):
        visited = set()
        result = dls(start, goal, depth, [start], visited)
        if result is not None:
            return result
    return None


initial = (2,8,3,1,6,4,7,"_",5)
goal = (1,2,3,8,"_",4,7,6,5)

solution = iddfs(initial, goal, max_depth=30)

if solution:
    print("Solution found in", len(solution)-1, "moves:\n")
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found within depth limit")
