from random import choice, randint


def game_logic():
    a = randint(0, 100)
    b = randint(0, 100)
    ops = ["+", "-", "*"]
    op = choice(ops)
    
    question = f"{a} {op} {b}"
    answer = str(eval(question))
                 
    return (question, answer)


def game():
    game_rule = 'What is the result of the expression?'    
    return game_rule, game_logic

