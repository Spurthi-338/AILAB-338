def main():
    all_perms = list(permutations(range(4)))
    print(f"Total permutations: {len(all_perms)}\n")

    while True:
        user_input = input("Enter initial state as 4 comma-separated integers from 0 to 3 (e.g. 1,3,0,2): ")
        try:
            user_state = tuple(int(x.strip()) for x in user_input.split(','))
            if len(user_state) != 4 or not is_valid_permutation(user_state):
                print("Invalid input! Please enter a permutation of 0,1,2,3 (each number exactly once).")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter integers separated by commas.")

    cost = compute_cost(user_state)
    print(f"\nYour input state: {user_state} | Diagonal Conflicts Cost: {cost}")
    print(print_board(user_state))
    print("-" * 30)

    print("Showing first 16 permutations with their costs:\n")
    for idx, perm in enumerate(all_perms[:16], 1):
        cost = compute_cost(perm)
        print(f"Case {idx}: {perm} | Diagonal Conflicts Cost: {cost}")
        print(print_board(perm))
        print("-" * 30)

if __name__ == "__main__":
    main()

