# 4 Years guarantees the saga of escaping F

GitHub link: https://github.com/D7NAMITE/4_years_guarantees

## Overview
4 Years Guarantees the saga of escaping F is the Text-based RPG game, inspired by the bittersweet life of Software Engineering student. The player will be roled as the "4 year'er" the legendary freshmen who the saga manifest you to dominate all the subjects. The player must defeat all the exam to held the title of "4 years guarantees".

## Requiments
For the game to run without any problem, you'll need:
- Python version 3.10 or later version
- game_script.csv file
- player_db.json file
- skill_info.json file
- enemy_db.json file
- time Module (Should be available as built-in Module) | command: time.sleep(sec)
- random Module (Should be available as built-in Module) | command: random.randint()
- os Module (Should be available as built-in Module) | command: os.system('cls')
- sys Module (Should be available as built-in Module) | command: sys.stdout.write(), sys.flush()

And for the best experience, I recommend you to:
- Run the game on **Command Propmt** (You can directly access the game through 'main_game.py' file, just click it.)
- Run the game in **Full-Screen**
- Set the font to **Courier New** size 16.

## Features
The game outstanding features are:
- Turn-base RPG gameplay: The player will expirience a turn-base fight just similar to the fight system on Pokemon battle.
- Story Prologue: The Prologue for the new player
- Text-tutorial and a tutorial round: The text explaination for player when they play the game for the first time. The player will met an easy level enemy in the first round to make them more used to to the game.
- Game Save Management: The game can manage player data. It can create the new game or load an existed game. The game will also save the updated data after the player win a fight.

## Gameplay
The game will be separated into two main phase the **Normal Phase** and the **Exam Phase**

### Normal Phase
The **Normal Phase** is the phase of calm and preperation. Player will use this phase to upgrade their attributes and develope some skill to be ready for the upcoming fight. 

The first interface the player will met is the attribute upgrading.
During this phase the player will get "5 Time Periods" per round which the player need to choose wheter to spend it on:
- Rest: +5 max HP (This doesn't include the healing)
- Study: +3 Intelligence Damage (ATK like attribute)
- Heal: Max health re-generate 

Next, the player will have an oppotunity to buy the **Special Move** which the player need to use their **Skill point** to earn one.
There're currently 4 moves that available in the game:
- A Cup of StrongBugs Coffees | 10 SP | +20 HP
- Revision Sheet | 30 SP | 50% chances of receiving 30 HP from enemy
- Grinding All Night | 50 SP | -25 HP to player, 75 Damage to enemy
- Wish Me Luck | 50 SP | 20% chance 100 Damage to enemy, 80% chance intake 75 Damage

### Exam Phase
The **Exam Phase** is when the brawl battle start. The player will face of and fight the "Subject". There will be 4 subjects (Did not include the tutorial subject), one each year.

The game will loop between this two phases untill the player defeat the 4th year subject.

## Technical Details
In this topic I'm going to cover about the details and function of each files and classes

### main_game.py
The main_game.py doesn't contain any class. It's work as a game runner where player can access through this file.

### character.py
The character.py consist of 3 classes
- Gauge class: The Gauge class is function as a 'Graphic' meter of the particular value. In the game the gauge will use for showing the player and enemy HP status.
- Player class: The player class is the class that will contain and manipulate the player attributes.
- Enemy class: The enemy class is the class that will contain and manipulate the enemy attributes.

### exam_phase.py
The exam_phase.py consist of 1 class
- Fight: Fight class is a class to manipulate a fight phase of each round. The fight are also known as an "Exam Phase" when player need to slaughter the exam. It's also included the player and enemy action, special move, critical, and more.

### main_menu.py
The main_menu.py consist of 2 classes and 1 function
- MainMenu: The MainMenu class is the class that will display and operate the main menu part of the game
- GaveSaveManager: The GameSaveManager class will manage the player data included, create a new player data, load an existed data, and save the updated data.
- typeprint(function): The typeprint function will create an typewritter effect display.

### normal_phase.py
The normal_phase.py consist of 2 classes
- Upgrade: The Upgrade class is the class that will operate and display the upgrading process.
- SkillStore: The SkillStore class is the class that will operate and display the skill store and skill buying process.
