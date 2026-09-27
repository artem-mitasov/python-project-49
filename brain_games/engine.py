import prompt

from brain_games.cli import welcome_user


def run_game(game):
    game_rule, game_logic = game()
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    
    print(game_rule)

    attempts_count = 3 
    while attempts_count > 0:

        question, correct_answer = game_logic()
        
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
            attempts_count -= 1
            continue
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. " 
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {user_name}!")
            break
        
    if attempts_count == 0:
        print(f"Congratulations, {user_name}!")

