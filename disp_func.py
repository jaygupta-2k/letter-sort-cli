import random
from tabulate import tabulate

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
