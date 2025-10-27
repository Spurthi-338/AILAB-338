def alpha_beta(node_index, depth, max_depth, alpha, beta, is_max, values, explored, pruned, path):
  

    # Number of leaves = 2^max_depth
    total_leaves = len(values)

    # If we reached a leaf node, return its value
    if depth == max_depth:
        leaf_index = node_index - (2 ** max_depth - 1)
        if 0 <= leaf_index < total_leaves:
            val = values[leaf_index]
            explored.append((list(path), val))
            return val
        else:
            return 0  # Safety fallback

    if is_max:
        value = float('-inf')
        for i in range(2):  # left & right children
            child_index = node_index * 2 + i + 1
            path.append(child_index)
            value = max(value, alpha_beta(child_index, depth + 1, max_depth,
                                          alpha, beta, False, values, explored, pruned, path))
            path.pop()
            alpha = max(alpha, value)
            if beta <= alpha:
                pruned.append((node_index, child_index, 'Beta cutoff'))
                break
        return value

    else:
        value = float('inf')
        for i in range(2):
            child_index = node_index * 2 + i + 1
            path.append(child_index)
            value = min(value, alpha_beta(child_index, depth + 1, max_depth,
                                          alpha, beta, True, values, explored, pruned, path))
            path.pop()
            beta = min(beta, value)
            if beta <= alpha:
                pruned.append((node_index, child_index, 'Alpha cutoff'))
                break
        return value


if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # leaf node values
    max_depth = 3                       # since 2^3 = 8 leaves
    explored, pruned = [], []
    print("Spurthi Reddy P : 1BM23CS338")
    print("Leaf node values:", values)

    result = alpha_beta(0, 0, max_depth, float('-inf'), float('inf'),
                        True, values, explored, pruned, [0])

    print("\nValue of root node (MAX mode):", result)
    print("\nExplored leaf paths:")
    for p, val in explored:
        print(f"Path {p} -> Value {val}")

    print("\nPruned branches:")
    for item in pruned:
        print(item)
