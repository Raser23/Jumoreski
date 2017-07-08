
import random
from collections import deque
import re


def generate_random_start(model):
    # Чтобы сгенерировать любое начальное слово, раскомментируйте строку:
    # return random.choice(model.keys())

    # Чтобы сгенерировать "правильное" начальное слово, используйте код ниже:
    # Правильные начальные слова - это те, что являлись началом предложений в корпусе
    if 'END' in model:
        seed_word = '#END#'
        while seed_word == '#END#':
            seed_word = model['#END#'].return_weighted_random_word()
        return seed_word
    return random.choice(list(model.keys()))


def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]

    if(length > 0):
        for i in range(0, length):
            current_dictogram = markov_model[current_word]
            random_weighted_word = current_dictogram.return_weighted_random_word()
            current_word = random_weighted_word
            sentence.append(current_word)
    else:
        count = 0
        while sentence[-1] != "#END#" and count < 500:
            count +=1
            current_dictogram = markov_model[current_word]
            random_weighted_word = current_dictogram.return_weighted_random_word()
            current_word = random_weighted_word
            sentence.append(current_word)

    sentence[0] = sentence[0].capitalize()
    return ' '.join(sentence) + '.'
    return sentence