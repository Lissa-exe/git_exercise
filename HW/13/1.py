from random import randint, choice
from typing import NamedTuple


class Weapon(NamedTuple):
    name: str
    power: int


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.durability = randint(3, 5)
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
        if other_warrior.durability:
            d_value = other_warrior.durability - self.weapon.power
            if d_value < 0:
                print('Оружие сломано. Достаёт новое.')
                random_choose_weapon()

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
        counter = 10

        while counter:
            print(kaeya.weapon.power, 'Кэйа, оружие')
            print(tartaglia.weapon.power, 'Тарталья, оружие')
            print(kaeya.health, 'Кэйа, здоровье')
            print(tartaglia.health, 'Тарталья, здоровье')
            print(kaeya.armor, 'Кэйа, броня')
            print(tartaglia.armor, 'Тарталья, броня')
            kaeya.heat_other(tartaglia)
            tartaglia.heat_other(kaeya)
            print(kaeya.durability, 'Кэйа, прочность оружия')
            print(tartaglia.durability, 'Тарталья, прочность оружия')
            if kaeya.health > tartaglia.health:
                print('Кэйа победил')
                pass
            else:
                print('Тарталья победил')
                pass
            print('раунд')
            if kaeya.health <= 0:
                print('Кэйа погиб')
                pass
            if tartaglia.health <= 0:
                print('Тарталья погиб')
                pass
            counter -= 1


main_fighting_area()
