import numpy as np
def game_core(number):
    count = 0
    low = 1
    high = 100
    predict = np.random.randint(low, high)
    while True:
        count += 1
        if predict == number:
            break
        elif predict > number:
            high = predict
            predict = np.random.randint(low, high)
        elif predict < number:
            low = predict
            predict = np.random.randint(low, high)
    return count

def score_game(game_core):
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_list.append(game_core(number))
    score = int(np.mean(count_list))
    print(f'Число попыток: {score}.')
    return score
print(score_game(game_core))
