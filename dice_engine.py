import random
def get_player_roll():
    """Get dice value from player (1–6)."""
    while True:
        try:
            value = int(input("Enter your dice value (1-6): "))
            if 1 <= value <= 6:
                return value
            else:
                print("Enter number between 1 and 6 only.")
        except ValueError:
            print("Invalid input. Enter a number.")
def get_computer_roll():
    """Generate dice value using random + modulus."""
    rand_num = random.randint(1, 100)
    return (rand_num % 6) + 1
def determine_winner(player, computer):
    """Compare values and return winner."""
    if player > computer:
        return "Player"
    elif computer > player:
        return "Computer"
    else:
        return "Tie"