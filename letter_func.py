def move_letters(source, destination):
    """
    Moves a letter from the source stack to the destination stack if valid.

    Args:
        source (list): The source stack.
        destination (list): The destination stack.

    Returns:
        bool: True if the move was successful, False otherwise.
    """
    flag = False

    if not source:
        return flag  # Cannot move from an empty stack

    while not destination or source[-1] == destination[-1]:
        destination.append(source.pop())
        flag = True
        if not source:
            break

    return flag  # Invalid move if colors don't match


def solvable_check(stack_list, max_stack_size):
    """
    Checks if the current game state is solvable by identifying valid moves.

    Args:
        stack_list (list of lists): The current state of the stacks.
        max_stack_size (int): The maximum allowed stack size.

    Returns:
        tuple: (source_index, destination_index) for a valid move, or None if no move exists.
    """
    for source_index, source_stack in enumerate(stack_list):
        if not source_stack:
            continue  # Skip empty stacks

        for destination_index, destination_stack in enumerate(stack_list):
            if source_index == destination_index:
                continue  # Skip the same stack

            if (not destination_stack or source_stack[-1] == destination_stack[-1]) and len(destination_stack) < max_stack_size:
                return source_index, destination_index

    return None  # No valid moves


if __name__ == "__main__":
    # Example usage
    stacks = [
        ["A", "B"],
        ["B"],
        [],
        []
    ]

    print("Before move:", stacks)
    move_letters(stacks[0], stacks[2])
    print("After move:", stacks)

    hint = solvable_check(stacks, 4)
    if hint:
        print(f"Hint: Move from stack {hint[0] + 1} to stack {hint[1] + 1}.")
    else:
        print("No valid moves available.")
