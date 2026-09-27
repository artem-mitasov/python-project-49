from random import randint


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def game_logic():
    num = randint(3, 100)
    question = str(num)
    
    if is_prime(num):
        answer = "yes"
    else:
        answer = "no"
    
    return (question, answer)
  
     
def game():
    game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return game_rule, game_logic

