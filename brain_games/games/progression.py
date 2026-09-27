from random import randint


def game_logic():
    start = randint(0, 100)
    diff = randint(-100, 100)
    progr_len = 10
    hid_idx = randint(0, progr_len - 1)

    num_list = [str(start)]
    for _ in range(1, progr_len):
        el = start + diff
        num_list.append(str(el))
        start = el
    answer = num_list[hid_idx]
    num_list[hid_idx] = '..'
    question = " ".join(num_list)
    
    return (question, answer)
     

def game():
    game_rule = 'What number is missing in the progression?'
    return game_rule, game_logic


