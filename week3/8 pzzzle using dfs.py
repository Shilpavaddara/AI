def dfs(state, goal, path, visited, depth):

    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            new_zero = nr * 3 + nc

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)

                result = dfs(
                    new_state,
                    goal,
                    path + [new_state],
                    visited,
                    depth - 1
                )

                if result:
                    return result

                visited.remove(new_state)

    return None


# Initial state
start = (5, 8, 2,
         1, 0, 3,
         4, 7, 6)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# DFS with maximum depth 10
solution = dfs(
    start,
    goal,
    [start],
    {start},
    10
)


# Display solution
if solution:

    print("DFS SOLUTION")
    print("============")

    for i, state in enumerate(solution):

        print("\nStep", i)
        print("-------")

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])

    print("\nTotal steps:", len(solution) - 1)
    print("Goal reached!")

else:
    print("No solution found within 10 steps.")
