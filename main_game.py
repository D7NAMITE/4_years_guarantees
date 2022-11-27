import json
import os
import time
import normal_phase
from main_menu import MainMenu, GameSaveManager
from character import Player


player = MainMenu().main_menu_interface()
player = normal_phase.Upgrade(player).upgrade_interface()
player = normal_phase.SkillStore(player).store_interface()
GameSaveManager().save_game(player)






