import json
import os
import sys
import time
from character import Player


def typeprint(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.03)
    print()


class MainMenu:
    def __init__(self, player_db='player_db.json', game_script='game_script.csv'):
        try:
            with open(player_db, 'r') as db_file:
                player_db_dict = json.load(db_file)
                self.__player_db = player_db_dict
        except FileNotFoundError:
            self.__file_existence = False
            print("[player_db.json] file  is missing")
            print("Please install [player_db.json] file\n")
        else:
            self.__file_existence = True

        try:
            with open(game_script) as game_script_file:
                script = []
                for row in game_script_file:
                    raw = row.splitlines()
                    for item in raw:
                        script += [item.split(',')]
            self.__game_script = script
        except FileNotFoundError:
            self.__file_existence = False
            print("[game_script.csv] file  is missing")
            print("Please install [game_script.csv] file\n")
        else:
            self.__file_existence = True

    def main_menu_interface(self):
        while True:
            if not self.__file_existence:
                break
            print(f'{"The legend of ":=<96}')
            print('''
    ░░██╗██╗   ██╗░░░██╗███████╗░█████╗░██████╗░░██████╗
    ░██╔╝██║   ╚██╗░██╔╝██╔════╝██╔══██╗██╔══██╗██╔════╝
    ██╔╝░██║   ░╚████╔╝░█████╗░░███████║██████╔╝╚█████╗░
    ███████║   ░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██╗░╚═══██╗
    ╚════██║   ░░░██║░░░███████╗██║░░██║██║░░██║██████╔╝
    ░░░░░╚═╝   ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
    
        ░██████╗░██╗░░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗████████╗███████╗███████╗░██████╗
        ██╔════╝░██║░░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝██╔════╝██╔════╝
        ██║░░██╗░██║░░░██║███████║██████╔╝███████║██╔██╗██║░░░██║░░░█████╗░░█████╗░░╚█████╗░
        ██║░░╚██╗██║░░░██║██╔══██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══╝░░██╔══╝░░░╚═══██╗
        ╚██████╔╝╚██████╔╝██║░░██║██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗███████╗██████╔╝
        ░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░
            ''')
            print(f'{" the saga of escaping F":=>96}')
            print('\n')
            print('Input [N] to start a new game')
            print('Input [L] to load an existed save')
            menu_decision = input(' : ')

            if menu_decision.lower() == 'n':
                os.system('cls')
                player = GameSaveManager().new_game()
                return player
            elif menu_decision.lower() == 'l':
                os.system('cls')
                player = GameSaveManager().load_game()
                return player
            else:
                for sec in range(3, 0, -1):
                    os.system('cls')
                    print('================================')
                    print('Invalid input please re-input in')
                    print(f'{sec:^32}')
                    print('================================')
                    time.sleep(1)
                os.system('cls')


class GameSaveManager:
    def __init__(self, player_db='player_db.json', game_script='game_script.csv'):
        self.__player_db = player_db
        self.__game_script = game_script
        self.__player = Player()
        with open(self.__player_db, 'r') as db_file:
            self.__player_db_dict = json.load(db_file)

    def new_game(self):
        # Prologue
        while True:
            print('And now, the sacred legend shall begin...')
            print('Input [S] to skip the prologue')
            print('Input [P] to play the "4 years guarantees saga"')
            skip_pro_decision = input(' : ')

            if skip_pro_decision.lower() == 's':
                os.system('cls')
                break
            elif skip_pro_decision.lower() == 'p':
                os.system('cls')
                with open(self.__game_script) as script_file:
                    script = []
                    for row in script_file:
                        raw = row.splitlines()
                        for item in raw:
                            script += [item.split(',')]
                for i in script:
                    try:
                        if i[1] == 'before_naming':
                            dialogue = i[0]
                            typeprint(f' {dialogue}')
                            time.sleep(0.75)
                    except IndexError:
                        continue
                break
            else:
                for sec in range(3, 0, -1):
                    os.system('cls')
                    print('================================')
                    print('Invalid input please re-input in')
                    print(f'{sec:^32}')
                    print('================================')
                    time.sleep(1)
                os.system('cls')

        while True:
            new_name = input('[Carve your name into the holy saga] : ')
            if new_name in self.__player_db_dict:
                for sec in range(3, 0, -1):
                    os.system('cls')
                    print('[Unfortunately, Your name was taken]')
                    print(f'Try again in {sec} sec')
                    time.sleep(1)
                os.system('cls')
            else:
                os.system('cls')
                typeprint('From the North to the South...')
                typeprint('From the Couch to the TV...')
                typeprint('From Discrete to Jogging...')
                typeprint(f'here comes our legend, "{new_name}" the 4-years-er')
                time.sleep(3)
                os.system('cls')
                new_player_info = {
                    new_name: {
                        "name": new_name,
                        "hp": 100,
                        "highest_hp": 100,
                        "atk": 10,
                        "coin": 0,
                        "year": 0
                    }
                }
                player = Player(new_name)
                self.__player_db_dict.update(new_player_info)
                with open(self.__player_db, 'w') as player_file:
                    json.dump(self.__player_db_dict, player_file, indent=4)
                self.__player = player
                return self.__player

    def load_game(self):
        while True:
            print('[To wake the sleeping holy saga, You must enter you name]')
            load_name = input(' : ')

            if load_name in self.__player_db_dict:
                os.system('cls')
                typeprint(f'Welcome back "{load_name}" the 4-years-er\n')
                player_info = self.__player_db_dict[load_name]
                player = Player(player_info['name'], player_info['hp'], player_info['highest_hp'],
                                player_info['atk'], player_info['coin'], player_info['year'],)
                self.__player = player
                print(player)
                print('\nInput [AnyKey] to continue')
                input(' : ')
                os.system('cls')
                return self.__player
            else:
                for sec in range(3, 0, -1):
                    os.system('cls')
                    print('[The saga has never seen your name]')
                    print(f'Try again in {sec} sec')
                    time.sleep(1)
                os.system('cls')

    def save_game(self, player):
        saving_player_info = {
            player.name: {
                "name": player.name,
                "hp": player.hp,
                "highest_hp": player.highest_hp,
                "atk": player.atk,
                "coin": player.coin,
                "year": player.year
            }
        }
        self.__player_db_dict.update(saving_player_info)
        with open('player_db.json', 'w') as player_file:
            json.dump(self.__player_db_dict, player_file, indent=4)
