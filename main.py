from utils import generate_secret_number, check_user_guess
from score import STARTING_SCORE, calculate_penalty, get_score_rating

secret_number = generate_secret_number()
current_score = STARTING_SCORE

while True:
    is_correct = check_user_guess(secret_number)

    if is_correct:
        rating = get_score_rating(current_score)
        print(f"\nCorrect! Final Score: {current_score}")
        print(f"Rating: {rating}")
        break
    else:
        current_score = calculate_penalty(current_score)
        print(f"Current Score: {current_score}\n")