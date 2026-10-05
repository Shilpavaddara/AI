def dls(state, goal, path, depth):

    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            new_zero = nr * 3 + nc
            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in path:
                result = dls(
                    new_state,
                    goal,
                    path + [new_state],
                    depth - 1
                )

                if result:
                    return result

    return None


def iddfs(start, goal, max_depth):

    for depth in range(max_depth + 1):
        result = dls(start, goal, [start], depth)

        if result:
            return result

    return None


# Initial state
start = (5, 8, 2,
         1, 0, 3,
         4, 7, 6)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# IDDFS
solution = iddfs(start, goal, 10)


# Output
if solution:

    print("IDDFS SOLUTION")
    print("==============")

    for step, state in enumerate(solution):

        print("\nStep", step)
        print("-------")

        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])

    print("\nTotal moves:", len(solution) - 1)
    print("Goal reached!")

else:
    print("No solution found.")
