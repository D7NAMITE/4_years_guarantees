import json
import os
import random
import time
from main_menu import typeprint


class Fight:
    """ Fight class is a class to manipulate a fight phase of each round.
    The fight are also known as an "Exam Phase" when player need to slaughter the exam.
    """
    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy
        with open('skill_info.json', 'r') as skill_file:
            self.__skill_info = json.load(skill_file)
        self.__enemy_buff = 0

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
        """ The function operate and display the Exam Phase interface.
        If the player play the game for the first time, the tutorial will occur.
        """
        if self.__player.year == 0:
            #  The Exam Phase tutorial.
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
            print('\nInput [Any Key] to continue')
            input(' : ')
        os.system('cls')
        os.system('mode con: cols=130 lines=55')  # This command will set the window size larger.

        turn = 1
        while True:
            print(f'Turn: {turn}')
            print('------------------------------------------------------------\n')
            print('-| Hostile |-')
            print(self.__enemy)
            print('\n========================= VS ===========================\n')
            print('-| 4-year-er |-')
            print(self.__player)
            print('\n------------------------------------------------------------')
            print('| Player Move |\n')
            print('Input [A] to perform an ordinary attack')
            order = 1
            for skill in self.__player.sp_move:
                print()
                print(f'Input [{order}] {self.__skill_info[skill]["name"]}')
                print(
                    f' >>> {self.__skill_info[skill]["effect"]} - {self.__skill_info[skill]["description"]}')
                print()
                order += 1
            print('============================================================')
            print(f'[{self.__player.name} Turn]')
            wrong_input = self.player_action()
            if wrong_input:
                # Check if player input the wrong value or not.
                continue
            if self.__enemy.hp <= 0:
                # Check if player defeated the enemy or not.
                os.system('cls')
                print(f'[Congratulation you have defeat {self.__enemy.name}]')
                self.__player.coin += self.__enemy.drop_coin
                print(f'Reward: {self.__enemy.drop_coin} Skill Points')
                print()
                print(self.__player)
                print()
                print('Enter [AnyKey]')
                input(' : ')
                os.system('cls')
                return self.__player
            print('============================================================')
            print(f'[{self.__enemy.name} Turn]')
            time.sleep(2)
            self.enemy_action()
            if self.__player.hp <= 0:
                # Check if player was defeated or not
                os.system('cls')
                print('''
    ░██████╗░░█████╗░███╗░░░███╗███████╗        ░█████╗░██╗░░░██╗███████╗██████╗
    ██╔════╝░██╔══██╗████╗░████║██╔════╝        ██╔══██╗██║░░░██║██╔════╝██╔══██╗
    ██║░░██╗░███████║██╔████╔██║█████╗░░        ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
    ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░        ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
    ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗        ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
    ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝        ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝''')
                print('Enter [Any Key] to exit')
                input(' : ')
                return 'GameOver'
            time.sleep(2)
            turn += 1
            print('============================================================')
            print('Input [AnyKey] to start the Next turn')
            input(' : ')
            os.system('cls')

    def player_action(self):
        """The method that will receive an input and respond the player action.
        Check of player input 'A' to perform an ordinary attack or '[number]' to performed an
        'Special Move'
        """
        while True:
            print('[Input here]')
            player_decision = input(' : ')
            try:
                int(player_decision)

            except ValueError:
                if player_decision.lower() == 'a':
                    self.player_attack()
                    print('[Ordinary Attack]')
                    time.sleep(1)
                    return False
                else:
                    for sec in range(3, 0, -1):
                        os.system('cls')
                        print('[Wrong input]')
                        print(f'Try again in {sec} sec')
                        time.sleep(1)
                    os.system('cls')
                    return True

            else:
                if int(player_decision) in range(1, len(self.__player.sp_move) + 1):
                    skill_using = self.__player.sp_move[int(player_decision) - 1]
                    print(f'[Special Move : {skill_using}]')
                    self.special_move_perform(skill_using)
                    time.sleep(1)
                    return False
                else:
                    for sec in range(3, 0, -1):
                        os.system('cls')
                        print('[Wrong input]')
                        print(f'Try again in {sec} sec')
                        time.sleep(1)
                    os.system('cls')
                    return True

    def special_move_perform(self, skill_using):
        """ The method operate when player perform a 'Special Move'
        """
        if skill_using == 'A Cup of StrongBugs Coffee':
            self.__player.hp += 20
            print(f'+20 HP Mental Stability to {self.__player.name}')

        elif skill_using == 'Revision Sheet':
            review_rate = random.randint(1, 2)
            if review_rate == 1:
                self.__enemy.hp -= 30
                self.__player.hp += 30
                print("This is I just wrote on the revision")
                print(f'+30 HP Mental Stability to {self.__player.name}')
                print(f'-30 HP to {self.__enemy.name}')
            else:
                print("Oh no! I didn't have this on my revision sheet...")
                print("No Effect Occur")

        elif skill_using == 'Grinding All Night':
            self.__player.hp -= 25
            self.__enemy.hp -= 75
            print(f'-20 HP Mental Stability for {self.__player.name}')
            print(f'75 Damage to {self.__enemy.name}')

        elif skill_using == 'Wish Me Luck':
            luck_rate = random.randint(1, 100)
            if luck_rate >= 30:
                self.__player.hp -= 25
                print('No luck...')
                print(f'25 Damage to {self.__player.name}')
            else:
                self.__enemy.hp -= 100
                print('Gotcha!!')
                print(f'100 Damage to {self.__enemy.name}')

    def player_attack(self, buff_percent=0):
        """The method that work if player perform an 'Ordinary Attack'.
        Also randomize the chance of getting extra 'Critical Damage'
        """
        crit_dmg = 0
        crit_chance = random.randint(1, 100)
        if crit_chance >= 85:
            crit_dmg = 10
            print(f'+{crit_dmg} Critical Damage!')
        pure_dmg = self.__player.atk + crit_dmg
        full_dmg = pure_dmg + (pure_dmg * (buff_percent / 100))
        print(f'{full_dmg:.0f} Damage to {self.__enemy.name}!')
        self.__enemy.hp -= full_dmg

    def enemy_action(self):
        """The method that will determine the enemy behaviour
        The enemy will start to consider healing themselves if the hp is lower than 50%
        """
        hp_percentage = (self.__enemy.hp / self.__enemy.highest_hp) * 100
        if hp_percentage < 50:
            heal_rate = random.randint(1, 100)
            if heal_rate >= 85:
                self.__enemy.hp += self.__enemy.heal_per_round
                print(f'{self.__enemy.name} heal for {self.__enemy.heal_per_round} hp')
            else:
                self.enemy_attack()
        else:
            self.enemy_attack()

    def enemy_attack(self):
        """The method that is work when enemy attack player
        """
        dmg = self.__enemy.atk + self.__enemy_buff
        self.__player.hp -= dmg
        print(f'{self.__enemy.name} makes {dmg} Damage')
