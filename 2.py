from collections import deque


def is_valid(m, c):
    """Check if missionaries and cannibals on a bank form a valid state."""
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    return True


def solve_missionaries_cannibals():
    initial_state = (3, 3, 0)  # (M_left, C_left, Boat_position)
    goal_state = (0, 0, 1)

    queue = deque([(initial_state, [])])
    visited = {initial_state}

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        current_state, path = queue.popleft()
        m_left, c_left, boat_pos = current_state

        if current_state == goal_state:
            return path + [current_state]

        for dm, dc in moves:
            if boat_pos == 0:  # Move from left to right
                next_m_left = m_left - dm
                next_c_left = c_left - dc
                next_boat_pos = 1
            else:  # Move from right to left
                next_m_left = m_left + dm
                next_c_left = c_left + dc
                next_boat_pos = 0

            next_m_right = 3 - next_m_left
            next_c_right = 3 - next_c_left

            next_state = (next_m_left, next_c_left, next_boat_pos)

            if (
                    is_valid(next_m_left, next_c_left)
                    and is_valid(next_m_right, next_c_right)
                    and next_state not in visited
            ):
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None


if __name__ == "__main__":
    solution_path = solve_missionaries_cannibals()

    if solution_path:
        print("Solution found:\n")
        for i, state in enumerate(solution_path):
            m_left, c_left, boat_pos = state
            m_right, c_right = 3 - m_left, 3 - c_left
            boat_side = "Left" if boat_pos == 0 else "Right"
            print(
                f"Step {i}: "
                f"Left Bank (M:{m_left}, C:{c_left}) | "
                f"Right Bank (M:{m_right}, C:{c_right}) | "
                f"Boat: {boat_side}"
            )
    else:
        print("No solution exists.")
