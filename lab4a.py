from collections import deque

def solve_puzzle_all_paths(initial, goal, max_depth=50):
    visited = set()
    initial_t = tuple(map(tuple, initial))
    visited.add(initial_t)
    
    queue = deque()
    queue.append((initial, [initial]))

    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
        
        if len(path) > max_depth:
            continue 
        
        neighbors_states = neighbors(current)
        misplaced_list = [(state, misplaced_tiles(state, goal)) for state in neighbors_states]
        
        if not misplaced_list:
            continue
        
        min_misplaced = min(m for _, m in misplaced_list)
        
        for state, m in misplaced_list:
            state_t = tuple(map(tuple, state))
            if m == min_misplaced and state_t not in visited:
                visited.add(state_t)
                queue.append((state, path + [state]))
    
    return None 

def main():
    initial_state = input_puzzle("initial")
    goal_state = input_puzzle("goal")

    print("\nInitial State:")
    print_state(initial_state)
    print("Goal State:")
    print_state(goal_state)

    misplaced = misplaced_tiles(initial_state, goal_state)
    print(f"Initial misplaced tiles count: {misplaced}\n")

    max_depth = int(input("Enter maximum search depth (e.g., 50): "))

    solution_path = solve_puzzle_all_paths(initial_state, goal_state, max_depth=max_depth)

    if solution_path is None:
        print("Could not solve the puzzle within the depth limit.")
    else:
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_state(state)

if __name__ == "__main__":
    main()
