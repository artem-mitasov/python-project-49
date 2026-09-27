from random import randint


def game_logic():
    a = randint(1, 100)
    b = randint(1, 100)
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i  
            
    question = f'{a} {b}'
    answer = str(gcd)
    
    return (question, answer)


def game():
    game_rule = 'Find the greatest common divisor of given numbers.'    
    return game_rule, game_logic
