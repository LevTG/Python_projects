# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice
from math import sqrt

def prost(a):
    d = 2
    while d <= sqrt(a):
        if a % d == 0:
            return 0
        d += 1 
    return 1
        

def mnog(a):
    answer = []
    d = 2
    while a != 1:
        if a % d == 0:
            answer.append(str(d))
            continue
        else:
            d += 1
    return ' '.join(answer)

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(str(x + y))
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 20
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(str(x - y))
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 30
        self._color = 'чёрный дракон'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(str(x * y))
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class Evil_Troll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._color = 'ужасный троль'

    def question(self):
        x = randint(1,5)
        self.__quest = "Угадай число от 1 до 5"
        self.set_answer(str(x))
        return self.__quest

class Bad_Troll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'злобный троль'

    def question(self):
        x = randint(1,100)
        self.__quest = "Число " + str(x) +  " простое? Если да, то введи 1. Если нет, то введи 0"
        if prost(x):
            self.set_answer(str(1))
        else:
            self.set_answer(str(0))
        return self.__quest


class Ugly_Troll(Troll):
    def __init__(self):
        self._health = 150
        self._attack = 10
        self._color = 'страшный троль'

    def question(self):
        x = randint(1,100)
        self.__quest = "Разложи число " + str(x) + " на множители и перечисли их через пробел"
        self.set_answer(mnog(x))
        return self.__quest

enemy_types = [Evil_Troll, Bad_Troll, Ugly_Troll, GreenDragon, RedDragon, BlackDragon]