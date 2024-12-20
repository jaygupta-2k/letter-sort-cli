import os
import random
from tabulate import tabulate

def welcome():
    """
    Displays the welcome message for the game.
    """
    c, l = os.get_terminal_size()
    header = " Color Sort Game "
    padding=c-len(header)
    left_pad=padding//2
    right_pad=padding-left_pad

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'-'*left_pad}{header}{'-'*right_pad}\n")
    print("Welcome to the Color Sort Game!")
    print("The goal is to sort colors into uniform stacks.\n")
    player_name = input("> Enter your name\n> ")
    print(f"\n> Hello, {player_name}! Let's begin.\n")
    return player_name

def stack_disp(stacks):
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
    # table.append(stack_labels)

    print(tabulate(table, headers=stack_labels, tablefmt="pretty", stralign="center", numalign="center"))

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
        "new":[],
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
    stack_disp(example_stacks)
    print(prompts(context="error"))
    print(prompts(context="restart"))
    print(prompts(context="transition"))
