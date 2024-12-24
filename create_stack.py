import random
from constants import *

def create_stack(num_stacks=None):
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


if __name__ == "__main__":
    # Example usage
    stacks = create_stack()
    for i, stack in enumerate(stacks):
        print(f"Stack {i + 1}: {stack}")
