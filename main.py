import utils

secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        break

from utils import generate_secret_number, check_user_guess

secret_number = generate_secret_number()

while True:
    if check_user_guess(secret_number):
        break

import utils
from score import update_score, get_rating

if __name__ == "__main__":
    secret_number = utils.generate_secret_number()
    score = 100

    guess = utils.prompt_valid_guess()
    while guess != secret_number:
        score = update_score(score)
        print(f"Wrong! Current score: {score}")
        guess = utils.prompt_valid_guess()

    print(f"You won! Final score: {score}")
    print(f"Rating: {get_rating(score)}")