# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = input(message)
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, evil_list):
    for dragon in evil_list:
        print('Вышел', dragon._color, '!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')
            if dragon.check_answer(answer):
                hero.attack(dragon)
                hero._experience += 50
                print('Верно! \n** враг кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print('Враг', dragon._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили! Сокровище ваше!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...\n')
        print('Тренируйтесь больше и вы сможете победить всех врагов и добраться до сокровища!')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        evil_number = 3
        evil_list = generate_dragon_list(evil_number)
        assert(len(evil_list) == 3)
        print('Путь к сокровищу преграждают', evil_number, 'врагов!')
        game_tournament(hero, evil_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
