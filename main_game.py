import json
from exam_phase import Fight
from main_menu import MainMenu, GameSaveManager
from normal_phase import Upgrade, SkillStore
from character import Enemy


def main():
    with open('enemy_db.json', 'r') as enemy_file:
        enemy_data = json.load(enemy_file)
    player = MainMenu().main_menu_interface()
    while True:
        stage = f'Year {player.year}'
        stage_enemy = enemy_data[stage]
        enemy = Enemy(stage_enemy['name'], stage_enemy['hp'], stage_enemy['highest_hp'],
                      stage_enemy['atk'], stage_enemy['year'], stage_enemy['heal_per_round'],
                      stage_enemy['drop_coin'])
        player = Upgrade(player).upgrade_interface()
        player = SkillStore(player).store_interface()
        player = Fight(player, enemy).fight_interface()
        if player == 'GameOver':
            break
        player.year += 1
        GameSaveManager().save_game(player)
        if player.year > 4:
            break


if __name__ == "__main__":
    main()
