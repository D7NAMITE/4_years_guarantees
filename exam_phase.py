import os
import time

from main_menu import typeprint


class Fight:
    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, new_player):
        self.__player = new_player

    @property
    def enemy(self):
        return self.__enemy

    @enemy.setter
    def enemy(self, new_enemy):
        self.__enemy = new_enemy

    def fight_interface(self):
        if self.__player.year == 0:
            with open('game_script.csv') as script_file:
                script = []
                for row in script_file:
                    raw = row.splitlines()
                    for item in raw:
                        script += [item.split(',')]
            for i in script:
                try:
                    if i[1] == 'exam_phase_explain':
                        dialogue = i[0]
                        typeprint(f' {dialogue}')
                        time.sleep(0.75)
                except IndexError:
                    continue
            print('\nInput [AnyKey] to continue')
            input_continue = input(' : ')
        os.system('cls')

