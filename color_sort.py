import re
from time import sleep
from create_stack import create_stack
from disp_func import *
from letter_func import move_letters, solvable_check
from constants import *

def main():
    """Main function to run the game."""
    player_name=welcome()
    # Game initialization
    while True:
        new = False
        stack_list = create_stack()
        original_stack_list = [stack.copy() for stack in stack_list]

        while True:
            stack_disp(stack_list)

            if all(is_solved(stack) for stack in stack_list if stack):
                print(f"\n> Congratulations, {player_name}! You solved the game.")
                new = input(f"\n> {prompts(context="repeat")}[Y/n]\n> ")
                break

            print("\n> "+prompts(context="transition"))
            command = input("> Enter your move (e.g., 1->2) or a command\n> ").strip().upper()

            if command == QUIT_COMMAND:
                break
            elif command == RESET_COMMAND:
                stack_list = [stack.copy() for stack in original_stack_list]
                print("\n> Game reset!")
                print("\n> "+prompts(context="restart"))
            elif command == HINT_COMMAND:
                hint = provide_hint(stack_list)
                print(hint)
            elif command == NEW_COMMAND:
                new = ''
                break
            elif command == INFO_COMMAND:
                print()
                how_to_play()
                sleep(5)
            else:
                try:
                    source, destination = parse_move(command)
                    if move_letters(stack_list[source], stack_list[destination]):
                        print(f"\n> Moved from stack {source + 1} to stack {destination + 1}.\n")
                    else:
                        print(f"\n> Invalid move. Please try again.\n> {prompts(context="error")}\n")
                except ValueError:
                    print(f"\n> Invalid input. Please use the format 1->2 or a valid command.\n> {prompts(context='error')}\n")

        if new not in ['Y','y','']:
            print(f"\n> Thanks for playing, {player_name}!")
            break
        else:
            print("\n> New game!\n")
            # print("> "+prompts(context="new"))
    # input()
    # os.system('cls' if os.name == 'nt' else 'clear')

def parse_move(command):
    """Parses the player's move command."""
    command = list(filter(str.strip, re.split(r'->|[,\-\s]',command)))
    if len(command) != 2:
        raise ValueError("Invalid move format.")

    source, destination = map(int, command)
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
        return f"\n> Hint: Try moving from stack {source + 1} to stack {destination + 1}."
    return "\n> No valid moves. Consider undoing or restarting."

if __name__ == "__main__":
    main()
