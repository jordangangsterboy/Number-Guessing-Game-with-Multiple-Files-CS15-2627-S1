STARTING_SCORE = 100
PENALTY = 10

def calculate_penalty(current_score: int):
    new_score = current_score - PENALTY

    if new_score < 0:
        return 0
    return new_score

def get_score_rating(final_score: int):
    if final_score >= 80:
        return "Excellent"
    elif final_score >= 50:
        return "Good"
    else:
        return "Keep practicing"


if __name__ == "__main__":
    print(calculate_penalty(100))
    print(calculate_penalty(5))

    print(get_score_rating(85))