from random import randint

import prompt

from brain_games.cli import welcome_user


def is_even(num):
    return num % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts_count = 3 
    while attempts_count > 0:
        guessed_number = randint(0, 100)
        print(f"Question: {guessed_number}")
        
        if is_even(guessed_number):
            correct_answer = "yes"
        else:
            correct_answer = "no"
        
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


if __name__ == "__main__":
    main()
