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
                    if i[1] == 'normal_phase_explain':
                        dialogue = i[0]
                        typeprint(f' {dialogue}')
                        time.sleep(0.75)
                except IndexError:
                    continue
            print('\nInput [AnyKey] to continue')
            input(' : ')
        os.system('cls')

        while True:
            print('_____________| Spend Some Time |_____________')
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
                GameSaveManager().save_game(self.__player)
                time.sleep(1)
                print('Auto saved')
                time.sleep(2)
                break
