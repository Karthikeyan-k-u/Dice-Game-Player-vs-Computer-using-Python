import os
FILE_NAME = "dice_scores.txt"
def save_score(winner):
    """Save winner to file."""
    with open(FILE_NAME, "a") as file:
        file.write(winner + "\n")

def get_scores():
    """Read and count scores."""
    scores = {"Player": 0, "Computer": 0, "Tie": 0}

    if not os.path.exists(FILE_NAME):
        return scores
    with open(FILE_NAME, "r") as file:
        for line in file:
            result = line.strip()
            if result in scores:
                scores[result] += 1
    return scores

def clear_scores():
    """Delete score file."""
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)