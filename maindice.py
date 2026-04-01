import dice_engine
import score_manager
import time

def show_menu():
    print("\n========== Dice Game ==========")
    print("1. Play Game")
    print("2. View Score History")
    print("3. Clear Score History")
    print("4. Exit")
    print("================================")
def play_game():
    print("\n Your Turn")
    player = dice_engine.get_player_roll()
    print("\n Computer Turn...")
    time.sleep(1)
    computer = dice_engine.get_computer_roll()
    print(f"\nYou rolled: {player}")
    print(f"Computer rolled: {computer}")
    winner = dice_engine.determine_winner(player, computer)
    if winner == "Tie":
        print(" It's a Tie!")
    else:
        print(f" Winner: {winner}")
    score_manager.save_score(winner)
def show_scores():
    scores = score_manager.get_scores()
    print("\n------ Score History ------")
    print(f"Player Wins   : {scores['Player']}")
    print(f"Computer Wins : {scores['Computer']}")
    print(f"Ties          : {scores['Tie']}")
    print("---------------------------")
def clear_history():
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        score_manager.clear_scores()
        print("History Cleared!")
def main():
    print("Welcome to Dice Game: Player vs Computer")
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")
        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            print("\nThanks for playing!")
            show_scores()
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()