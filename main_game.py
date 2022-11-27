import json
import os
import time
import normal_phase
from main_menu import MainMenu
from character import Player


player = MainMenu().main_menu_interface()
normal_phase.Upgrade(player).upgrade_interface()




