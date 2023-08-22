import random
from logo import high_lower, versus
from hiogh_lower_dict import data

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    print(f"{name}, a {description}, from {country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(high_lower)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(versus)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who have more follower? Type 'A' or 'B'").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're rigth! Current score {score}\n")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. The final score: {score}")

game()

