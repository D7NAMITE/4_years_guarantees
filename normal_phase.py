import json
import os
import time
from character import Player
from main_menu import typeprint, GameSaveManager


class Upgrade:
    def __init__(self, player, player_db='player_db.json', game_script='game_script.csv',
                 time_pt=5):
        self.__player = player
        self.__player_db = player_db
        self.__game_script = game_script
        self.__time_pt = time_pt

    def attribute_upgrade(self):
        print('=============================================')
        print('[Input here]')
        upgrade_selection = input(' : ')
        if upgrade_selection.lower() == 'r':
            self.__player.highest_hp += 5
            self.__time_pt -= 1
            print('[+5 Mental Stability]')
            time.sleep(0.5)
            os.system('cls')
        elif upgrade_selection.lower() == 's':
            self.__player.atk += 3
            self.__time_pt -= 1
            print('[+3 Intelligent Damage]')
            time.sleep(0.5)
            os.system('cls')
        elif upgrade_selection.lower() == 'h':
            self.__player.hp = self.__player.highest_hp
            self.__time_pt -= 1
            print('[Fully-Heal Mental Stability]')
            time.sleep(0.5)
            os.system('cls')
        else:
            for sec in range(3, 0, -1):
                os.system('cls')
                print('[Wrong input]')
                print(f'Try again in {sec} sec')
                time.sleep(1)
            os.system('cls')

    def upgrade_interface(self):
        if self.__player.year == 0:
            with open(self.__game_script) as script_file:
                script = []
                for row in script_file:
                    raw = row.splitlines()
                    for item in raw:
                        script += [item.split(',')]
            for i in script:
                try:
                    if i[1] == 'upgrade_explain':
                        dialogue = i[0]
                        typeprint(f' {dialogue}')
                        time.sleep(0.75)
                except IndexError:
                    continue
            print('\nInput [AnyKey] to continue')
            input(' : ')
        os.system('cls')

        while True:
            print('_____________| Time Management |_____________')
            print()
            print(f'{"Time Period: " + str(self.__time_pt):^45}')
            print('_____________________________________________')
            print()
            print('Input [R] to rest')
            print('>>> +5 Max Mental Stability | 1 time period')
            print()
            print('Input [S] to study')
            print('>>> +3 Intelligent Damage | 1 time period')
            print()
            print('Input [H] to Mental Healing')
            print('>>> Fully-Heal Mental Stability | 1 time period')
            print()
            print('==============================================')
            print()
            print(self.__player)
            print()
            self.attribute_upgrade()
            if self.__time_pt == 0:
                os.system('cls')
                print(self.__player)
                time.sleep(1)
                print('\nInput [AnyKey] to continue')
                input(' : ')
                os.system('cls')
                return self.__player


class SkillStore:
    def __init__(self, player, player_db='player_db.json', game_script='game_script.csv'):
        self.__player = player
        self.__player_db = player_db
        self.__game_script = game_script
        with open('skill_info.json', 'r') as skill_file:
            self.__skill_info = json.load(skill_file)
        self.__skill_lst = [skill for skill in self.__skill_info if skill not in self.__player.sp_move]

    def store_interface(self):
        if self.__player.year == 0:
            with open(self.__game_script) as script_file:
                script = []
                for row in script_file:
                    raw = row.splitlines()
                    for item in raw:
                        script += [item.split(',')]
            for i in script:
                try:
                    if i[1] == 'skill_store_explain':
                        dialogue = i[0]
                        typeprint(f' {dialogue}')
                        time.sleep(0.75)
                except IndexError:
                    continue
            print('\nInput [Any Key] to continue')
            input(' : ')
        os.system('cls')

        while True:
            if len(self.__skill_lst) == 0:
                typeprint(f'You have bought all skills\n')
                time.sleep(2)
                break
            print('_______________| Skill Store |_______________')
            print(f'\n{"Skill Points: " + str(self.__player.coin):^45}')
            print('_____________________________________________')
            print()
            print('Input [number] of the skill to buy')
            print('Input [x] to exit the store')
            order = 1
            for skill in self.__skill_info:
                if skill in self.__skill_lst:
                    print()
                    print(f'[{order}] {self.__skill_info[skill]["name"]} | '
                          f'{self.__skill_info[skill]["cost"]} Skill Points')
                    print(f' >>> {self.__skill_info[skill]["effect"]} - '
                          f'{self.__skill_info[skill]["description"]}')
                    print()
                    order += 1
            stop_or_not = self.skill_buying()
            if stop_or_not:
                os.system('cls')
                break
            os.system('cls')
        print(self.__player)
        time.sleep(1)
        print('\nInput [AnyKey] to continue')
        input(' : ')
        os.system('cls')
        return self.__player

    def skill_buying(self):
        print('==============================================')
        print('[Input here]')
        buy_decision = input(' : ')
        try:
            int(buy_decision)
        except ValueError:
            if buy_decision.lower() == 'x':
                return True
            else:
                for sec in range(3, 0, -1):
                    os.system('cls')
                    print('[Wrong input]')
                    print(f'Try again in {sec} sec')
                    time.sleep(1)
                os.system('cls')
        else:
            if int(buy_decision) in range(1, len(self.__skill_lst)+1):
                price = self.__skill_info[self.__skill_lst[int(buy_decision) - 1]]["cost"]
                if self.__player.coin < price:
                    for sec in range(3, 0, -1):
                        os.system('cls')
                        print('[Not enough money]')
                        print(f'Try again in {sec} sec')
                        time.sleep(1)
                    os.system('cls')
                else:
                    self.__player.sp_move += [self.__skill_lst[int(buy_decision)-1]]
                    self.__player.coin -= price
                    bought = self.__skill_lst.pop(int(buy_decision)-1)
                    print(f'[You have bought {bought}]')
                    time.sleep(1)
            else:
                for sec in range(3, 0, -1):
                    os.system('cls')
                    print('[Wrong input]')
                    print(f'Try again in {sec} sec')
                    time.sleep(1)
                os.system('cls')
