"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить здоровья, сменить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
Следует учесть:
 - у воина может быть броня
 - здоровье не может быть меньше 0
 - броня не может быть меньше 0
 - здоровье не тратится пока броня не 0
Было бы неплохо добавить возможность воину носить несколько видов оружия и при сломаном текущем заменить его (опционально)
"""
from random import randint, choice
from typing import NamedTuple


class Weapon(NamedTuple):
    name: str
    power: int


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = randint(5, 10)
        self.status = 'alive'

    def add_health(self, value):
        if value < 0:
            print('Слишком мало')
            return
        self.health += value

    def change_weapon(self, weapon):
        self.weapon = weapon

    def add_armor(self, armor):
        if armor < 0:
            print('Слишком мало')
            return
        self.armor += armor

    def heat_other(self, other_warrior):
        if other_warrior.status == 'die':
            print(other_warrior.name + ' погиб')
            raise Exception
        if other_warrior.armor:
            armor_value = other_warrior.armor - self.weapon.power
            if armor_value < 0:
                other_warrior.armor -= self.weapon.power + armor_value
                other_warrior.health += armor_value
                print('Броня сломана')
                return
            other_warrior.armor -= self.weapon.power
            return
        health_value = other_warrior.health - self.weapon.power
        if health_value < 0:
            other_warrior.status = 'die'
            return
        other_warrior.health -= self.weapon.power

def random_choose_weapon():
    weapon_list = []
    for i in range(10):
        weapon_list.append(Weapon(
            name=str(i),
            power=randint(1, 10)
        ))
    return choice(weapon_list)



def main_fighting_area():
    start = input('Начать драку? \n')
    kaeya = Warrior(name='Кэйа', health=10, weapon=random_choose_weapon())
    tartaglia = Warrior(name='Тарталья', health=10, weapon=random_choose_weapon())
    if start == 'да':
        counter = 5

        while counter:
            print(kaeya.weapon.power, 'Кэйа, оружие')
            print(tartaglia.weapon.power, 'Тарталья, оружие')
            print(kaeya.health, 'Кэйа, здоровье')
            print(tartaglia.health, 'Тарталья, здоровье')
            print(kaeya.armor, 'Кэйа, броня')
            print(tartaglia.armor, 'Тарталья, броня')
            kaeya.heat_other(tartaglia)
            tartaglia.heat_other(kaeya)
            print('раунд')
            counter -= 1


main_fighting_area()
