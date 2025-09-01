def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(state[i:i+3]))
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

def dfs(start_state, max_depth=20):
    visited = set()
    stack = [(start_state, [], [], 0)]  # (state, path, moves, depth)

    while stack:
        current_state, path, moves, depth = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if is_goal(current_state):
            steps = path + [current_state]
            print("\nGoal reached (DFS)!\n")
            for i, step in enumerate(steps):
                print(f"Step {i}:")
                print_state(step)
            print("Moves:", " -> ".join(moves))
            print("Total steps to goal:", len(steps) - 1)
            print("Total unique states visited:", len(visited))
            return

        if depth < max_depth:
            for neighbor, move in reversed(get_neighbors(current_state)):
                if neighbor not in visited:
                    stack.append((neighbor, path + [current_state], moves + [move], depth + 1))

    print(f"No solution found within depth limit of {max_depth}!")
start = "283164705"
dfs(start, max_depth=20)
