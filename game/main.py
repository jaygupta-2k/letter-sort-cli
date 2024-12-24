from time import sleep
from .display import *
from .game_logic import *
from .constants import *

def main():
    """Main function to run the game."""
    player_name=welcome()
    # Game initialization
    while True:
        new = False
        stack_list = initialize_game()
        original_stack_list = [stack.copy() for stack in stack_list]

        while True:
            show_stacks(stack_list)

            if all(check_win_condition(stack) for stack in stack_list if stack):
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
                    if process_move(stack_list[source], stack_list[destination]):
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

if __name__ == "__main__":
    main()
