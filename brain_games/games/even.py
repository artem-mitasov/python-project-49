from random import randint


def is_even(num):
    return num % 2 == 0


def game_logic():
    num = randint(0, 100)
    question = str(num)
    
    if is_even(num):
        answer = "yes"
    else:
        answer = "no"
                 
    return (question, answer)


def game():
    game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    return game_rule, game_logic