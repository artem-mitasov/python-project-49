import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game):
    game_rule, game_logic = game()
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    
    print(game_rule)

    rounds_left = ROUNDS_COUNT
    while rounds_left > 0:

        question, correct_answer = game_logic()
        
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
            rounds_left -= 1
            continue
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. " 
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {user_name}!")
            break
        
    if rounds_left == 0:
        print(f"Congratulations, {user_name}!")

