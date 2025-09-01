from collections import deque
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def is_goal(state):
    return state == "123804765"

def get_neighbors(state):
    neighbors = []
    moves = {'Up': -3, 'Down': 3, 'Left': -1, 'Right': 1}
    zero_index = state.index('0')
   
    for move, pos_change in moves.items():
        new_index = zero_index + pos_change
        if move == 'Left' and zero_index % 3 == 0:
            continue
        if move == 'Right' and zero_index % 3 == 2:
            continue
        if move == 'Up' and zero_index < 3:
            continue
        if move == 'Down' and zero_index > 5:
            continue
        state_list = list(state)
        state_list[zero_index], state_list[new_index] = state_list[new_index], state_list[zero_index]
        neighbors.append(("".join(state_list), move))
    return neighbors

def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [], [])])  # (current_state, path_of_states, moves_taken)

    while queue:
        current_state, path, moves = queue.popleft()

        if current_state in visited:
            continue
        visited.add(current_state)

        if is_goal(current_state):
            steps = path + [current_state]
            print("\n Goal reached!\n")
            for i, step in enumerate(steps):
                print(f"Step {i}:")
                print_state(step)
            print("Moves:", " -> ".join(moves))
            print("Total steps to goal:", len(steps) - 1)
            print("Total unique states visited:", len(visited))
            return

        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state], moves + [move]))

    print("No solution found!")

start = "283164705"
bfs(start)
