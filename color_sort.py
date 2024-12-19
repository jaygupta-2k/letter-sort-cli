import random
from os import system
from create_stack import create_stack
from disp_func import stack_disp, prompts
from letter_func import move_letters, solvable_check

# Constants for the game
MAX_STACK_SIZE = 4
QUIT_COMMAND = 'Q'
RESET_COMMAND = 'R'
HINT_COMMAND = 'H'
NEW_COMMAND = 'N'

def main():
    system('clear;')
    print("Welcome to the Color Sort Game!")
    player_name = input("> Enter your name\n> ")
    print(f"> Hello, {player_name}! Let's begin.")

    # Game initialization
    while True:
        new = False
        stack_list = create_stack()
        original_stack_list = [stack.copy() for stack in stack_list]

        while True:
            stack_disp(stack_list)
            print("> "+prompts(context="transition"))

            if all(is_solved(stack) for stack in stack_list if stack):
                print(f"> Congratulations, {player_name}! You solved the game.")
                new = input(f"> {prompts(context="repeat")}[Y/n]\n> ")
                break

            command = input("> Enter your move (e.g., 1->2) or a command (H for hint, R to reset, Q to quit, N to start a new game)\n> ").strip().upper()

            if command == QUIT_COMMAND:
                print(f"> Thanks for playing, {player_name}!")
                break
            elif command == RESET_COMMAND:
                stack_list = [stack.copy() for stack in original_stack_list]
                print("> Game reset!")
                print("> "+prompts(context="restart"))
            elif command == HINT_COMMAND:
                hint = provide_hint(stack_list)
                print(hint)
            elif command == NEW_COMMAND:
                print("> New game!")
                # print("> "+prompts(context="new"))
                new = ""
                break
            else:
                try:
                    source, destination = parse_move(command)
                    if move_letters(stack_list[source], stack_list[destination]):
                        print(f"> Moved from stack {source + 1} to stack {destination + 1}.")
                    else:
                        print("> Invalid move. Please try again.")
                        print("> "+prompts(context="error"))
                except ValueError:
                    print("> Invalid input. Please use the format 1->2 or a valid command.")
                    print("> "+prompts(context="error"))

        if new not in ['Y','y',""]:
            break

def parse_move(command):
    """Parses the player's move command."""
    if '->' not in command or len(command.split('->')) != 2:
        raise ValueError("Invalid move format.")

    source, destination = map(int, command.split('->'))
    source_index = source - 1
    destination_index = destination - 1

    return source_index, destination_index

def is_solved(stack):
    """Checks if a stack is solved (contains one type of color and is full)."""
    return len(stack) == MAX_STACK_SIZE and len(set(stack)) == 1

def provide_hint(stacks):
    """Generates a hint for the player based on the current stack configuration."""
    solvable_move = solvable_check(stacks, MAX_STACK_SIZE)
    if solvable_move:
        source, destination = solvable_move
        return f"> Hint: Try moving from stack {source + 1} to stack {destination + 1}."
    return "> No valid moves. Consider undoing or restarting."

if __name__ == "__main__":
    main()
