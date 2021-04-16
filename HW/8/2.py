import random
import json

def first_player():
    input('Игрок 1, ваш ход')
    return random.randint(1, 6)

def second_player():
    input('Игрок 2, ваш ход')
    return random.randint(1, 6)

def main():
    start = input('Start game yes|no')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':
        first_round = {}
        counter = 3

        while counter:
            player_1_value = first_player()
            player_2_value = second_player()
            if player_1_value == player_2_value:
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value

            print(player_1_value)
            print(player_2_value)

            counter -= 1
            first_round[f'round_{3 -counter}'] = {"First player": player_1_value,
                           "Second player": player_2_value,
                           "Final": player_1_sum,
                           "Final2": player_2_sum}

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(first_round, f, ensure_ascii=False, indent=4)

        if player_1_sum > player_2_sum:
            print(' First player win')
            print(player_1_sum)
            print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print('Friendship win')
            print(player_1_sum)
            print(player_2_sum)
            return

        print(' Second player win')
        print(player_1_sum)
        print(player_2_sum)

main()