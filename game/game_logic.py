import random
import re
from .constants import *

def initialize_game(num_stacks=None):
    """
    Generates the initial game state with randomized stacks.

    Args:
        num_stacks (int, optional): Number of stacks to generate. Defaults to a random number between MIN_STACKS and MAX_STACKS.

    Returns:
        list of lists: A list of stacks representing the game state.
    """
    if num_stacks is None:
        num_stacks = random.randint(MIN_STACKS, MAX_STACKS)

    # Choose a subset of colors based on the number of stacks
    num_colors = num_stacks - 2
    selected_colors = COLORS[:num_colors]

    # Create a pool of colors with each appearing exactly MAX_STACK_SIZE times
    color_pool = selected_colors * MAX_STACK_SIZE
    random.shuffle(color_pool)

    # Generate stacks and ensure no stack is fully uniform
    stacks = []
    while color_pool:
        stack = []
        while len(stack) < MAX_STACK_SIZE and color_pool:
            color = color_pool.pop()
            stack.append(color)

        # Validate stack uniformity
        if len(set(stack)) == 1:
            color_pool.extend(stack)
            random.shuffle(color_pool)
            continue

        stacks.append(stack)

    # Add empty stacks for player moves
    for _ in range(2):
        stacks.append([])

    return stacks


def process_move(source, destination):
    """
    Moves a letter from the source stack to the destination stack if valid.

    Args:
        source (list): The source stack.
        destination (list): The destination stack.

    Returns:
        bool: True if the move was successful, False otherwise.
    """
    flag = False

    if not source or len(destination) == MAX_STACK_SIZE:
        return flag  # Cannot move from an empty stack or to stack of max length

    while (not destination or source[-1] == destination[-1]) and len(destination) != MAX_STACK_SIZE:
        destination.append(source.pop())
        flag = True
        if not source:
            break

    return flag  # Invalid move if colors don't match


def check_solvability(stack_list, max_stack_size):
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


def parse_move(command):
    """Parses the player's move command."""
    command = list(filter(str.strip, re.split(r'->|[,\-\s]',command)))
    if len(command) != 2:
        raise ValueError("Invalid move format.")

    source, destination = map(int, command)
    source_index = source - 1
    destination_index = destination - 1

    return source_index, destination_index


def check_win_condition(stack):
    """Checks if a stack is solved (contains one type of color and is full)."""
    return len(stack) == MAX_STACK_SIZE and len(set(stack)) == 1


def provide_hint(stacks):
    """Generates a hint for the player based on the current stack configuration."""
    solvable_move = check_solvability(stacks, MAX_STACK_SIZE)
    if solvable_move:
        source, destination = solvable_move
        return f"\n> Hint: Try moving from stack {source + 1} to stack {destination + 1}."
    return "\n> No valid moves. Consider undoing or restarting."


if __name__ == "__main__":
    # Example usage
    stacks = initialize_game()
    for i, stack in enumerate(stacks):
        print(f"Stack {i + 1}: {stack}")

    print("Before move:", stacks)
    process_move(stacks[0], stacks[2])
    print("After move:", stacks)

    hint = check_solvability(stacks, 4)
    if hint:
        print(f"Hint: Move from stack {hint[0] + 1} to stack {hint[1] + 1}.")
    else:
        print("No valid moves available.")
