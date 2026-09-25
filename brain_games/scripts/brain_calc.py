from random import randint, choice

import prompt

from brain_games.cli import welcome_user


def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
            return a - b
    else:
        return a * b


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    print(f"Hello, {user_name}!")
    
    print('What is the result of the expression?')
    
    attempts_count = 3 
    while attempts_count > 0:
        
        ops = ["+","-","*"]
        op = choice(ops)
        a = randint(0, 100)
        b = randint(0, 100)
        print(f"Question: {a} {op} {b}")

        correct_answer = str(calc(a, b, op))
        
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
