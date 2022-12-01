# 4 Years guarantees the saga of escaping F

## Overview
4 Years Guarantees the saga of escaping F is the Text-based RPG game, inspired by the bittersweet life of Software Engineering student. The player will be roled as the "4 year'er" the legendary freshmen who the saga manifest you to dominate all the subjects. The player must defeat all the exam to held the title of "4 years guarantees".

## Features
The game outstading features are:
- Turn-base RPG gameplay: The player will expirience a turn-base fight just similar to the fight system on Pokemon battle.
- Story Prologue: The Prologue for the new player
- Text-tutorial and a tutorial round: The text explaination for player when they play the game for the first time. The player will met an easy level enemy in the first round to make them more used to to the game.
- Game Save Management: The game can manage player data. It can create the new game or load an existed game. The game will also save the updated data after the player win a fight.

## Gameplay
The game will be separated into two main phase the **Normal Phase** and the **Exam Phase**

The **Normal Phase** is the phase of calm and preperation. Player will use this phase to upgrade their attributes and develope some skill to be ready for the upcoming fight.

In the other hand, the **Exam Phase** is when the brawl battle start. The player will face of and fight the "Subject". There will be 4 subjects(Did not include the tutorial subject), one each year.

The game will loop between this two phases untill the player defeat the 4th year subject. 

## Requiments
For the game to run without any problem, you'll need:
- Python version 3.10 or later version
- game_script.csv file
- player_db.json file
- skill_info.json file
- enemy_db.json file
- time Module (Should be available as built-in Module)
- random Module (Should be available as built-in Module)
- os Module (Should be available as built-in Module)
- sys Module (Should be available as built-in Module)

And for the best experience, I recommend you to:
- Run the game on **Command Propmt** (You can directly access the game through 'main_game.py' file, just click it.)
- Run the game in **Full-Screen**
- Set the font to **Courier New** size 16.

## Technical Details
In this topic I'm going to cover about the details and function of each files and classes
### character.py
The character.p consist of 3 classes
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
