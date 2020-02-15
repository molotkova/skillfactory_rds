import numpy as np
def game_core_2(number):
    count = 0
    bound = 100
    predict = np.random.randint(1, bound)
    while True:
        count += 1
        if predict == number:
            break
        elif predict > number:
            predict -= 1
            if predict + 1 > bound / 2:
                predict = np.random.randint(1, bound / 2)  # отрезаем из рассмотрения всё, что справа
            else:
                predict = np.random.randint(1, predict + 1)
        elif predict < number:
            predict += 1
            if predict - 1 < bound / 2:
                predict = np.random.randint(bound / 2, 100)
            else:
                predict = np.random.randint(predict - 1, 100)
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