import os
import random
from tabulate import tabulate
from colorama import Style, Fore, Back
from .constants import MAX_STACK_SIZE

def welcome():
    """
    Displays the welcome message for the game.
    """
    c, l = os.get_terminal_size()
    header = " Letter Sort Game "
    padding=c-len(header)
    left_pad=padding//2
    right_pad=padding-left_pad

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.WHITE+f"{'-'*left_pad}{header}{'-'*right_pad}\n")
    print("Welcome to the Letter Sort Game!\n")
    how_to_play()
    player_name = input("> Enter your name\n> ")
    print(f"\n> Hello, {player_name}! Let's begin.\n")
    return player_name


def how_to_play():
    """
    Displays the "how to play?" message
    """
    print("How to play?")
    print("The goal is to sort letters into uniform stacks.")
    print(f"Each stack can contain a maximum of {MAX_STACK_SIZE} letters.")
    print("You can only move the top letter of a stack.")
    print("The letter can be moved to a stack with the same letter on top or to an empty stack.\n")
    print("You can enter your move in one of these formats")
    print("  1-2 or 1,2 or 1 2 or 1->2\n")
    print("Or you can enter a command")
    print("  R: Reset the game.")
    print("  Q: Quit the game.")
    print("  H: Get a hint.")
    print("  I: To display this message.\n")


def show_stacks(stacks):
    """
    Displays the current state of the stacks in a tabular format.

    Args:
        stacks (list of lists): The current state of the game stacks.
    """
    max_height = max(len(stack) for stack in stacks)
    table = []

    for i in range(max_height - 1, -1, -1):
        row = []
        for stack in stacks:
            row.append(stack[i] if i < len(stack) else " ")
        table.append(row)

    stack_labels = [i + 1 for i in range(len(stacks))]
    sep = ["---" for i in range(len(stacks))]
    table.append(sep)
    table.append(stack_labels)

    print(tabulate(table, tablefmt="rounded_outline", stralign="center", numalign="center"))


def prompts(context="error"):
    """
    Returns a random prompt from a predefined list based on the context.

    Args:
        context (str): The type of prompt to return. Options are 'error', 'restart', 'transition'.

    Returns:
        str: A randomly selected prompt.
    """
    prompt_pool = {
        "error": [
            "Oops! That move didn't work. Try again.",
            "Invalid move! Think carefully.",
            "Hmm, that didn't go as planned. Give it another shot.",
            "Not quite right! Let's focus and retry.",
            "Mistakes happen! Reevaluate your strategy and try again."
        ],
        "restart": [
            "Fresh start! Let's see if this time works better.",
            "Game reset. Focus and plan ahead!",
            "Restarting the game. You got this!",
            "Here we go again! Time to crack the puzzle.",
            "Reset complete. Take a deep breath and dive in!"
        ],
        "transition": [
            "Let's make the next move count!",
            "Great effort! Ready for the next step?",
            "Take your time and think about your next move.",
            "You're doing well! Keep the momentum going.",
            "Progress is progress. Let's aim for the solution!"
        ],
        "new":[
            "All the best!",
            "Best of luck!",
            "Break a leg!"
        ],
        "repeat":[
            "Ready for a rematch?",
            "Fancy another game?",
            "Up for another round?",
            "How about another go?",
            "Wanna play again?",
			"Another round?",
			"Care for another game?",
			"Want another round?",
			"How about a rematch?",
			"Up for it again?",
			"Ready for another round?"
		],
    }

    return random.choice(prompt_pool.get(context, ["Keep going!"]))

if __name__ == "__main__":
    # Example usage
    example_stacks = [
        ["A", "B", "C"],
        ["B", "C"],
        ["A"],
        []
    ]
    show_stacks(example_stacks)
    print(prompts(context="error"))
    print(prompts(context="restart"))
    print(prompts(context="transition"))
    print(prompts(context="repeat"))
