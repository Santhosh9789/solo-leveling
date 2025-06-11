# Solo Leveling System - Game Core

This project is a Python-based implementation of a core game system inspired by the mechanics found in the popular manhwa "Solo Leveling". It aims to replicate features such as player leveling, stat progression, skill acquisition, and more.

This is the first phase of development, focusing on the foundational elements of the system.

## Core Features (Phase 1)

This initial phase implements the following core features:

*   **Player Class:**
    *   Manages player attributes: `level`, `experience (XP)`, `stats` (Strength, Agility, Intelligence, Stamina, Perception), `HP` (Health Points), `MP` (Mana Points).
    *   HP and MP are automatically calculated based on Stamina and Intelligence, respectively.
*   **Stat Upgrades:**
    *   Functionality to increase a player's base stats.
*   **Leveling System:**
    *   Players gain XP by defeating enemies.
    *   Upon reaching experience thresholds, players `level up`.
    *   Leveling up grants `stat points` that can be allocated (though allocation mechanism is for a future phase, points are accrued).
    *   Excess XP is carried over to the next level.
*   **Skill Acquisition:**
    *   Players automatically learn new `skills` upon reaching specific level milestones.
    *   Skills are defined with names, descriptions, and level requirements.
*   **Basic Enemy Interaction:**
    *   A simple `Enemy` class allows defining enemies with stats and XP rewards.
    *   Players can conceptually `attack` and `defeat` enemies to gain XP.
*   **Notification System:**
    *   A console-based `notification system` provides feedback for game events like leveling up, gaining XP, and learning skills.
*   **Unit Tests:**
    *   A suite of unit tests (`tests/test_player.py`) ensures the core player mechanics function as expected.

## How to Run

To see a basic demonstration of the system:

1.  **Prerequisites:**
    *   Ensure you have Python 3.x installed on your system.
2.  **Navigate to Project Directory:**
    *   Open your terminal or command prompt.
    *   Change directory to the root of this project (where `main.py` is located).
3.  **Run the Script:**
    *   Execute the following command:
        ```bash
        python main.py
        ```
    *   This will simulate a player character encountering and defeating an enemy, gaining experience, potentially leveling up, and unlocking skills. The output will be displayed in the console.

## Project File Structure

*   `player.py`: Contains the `Player` class, which defines the attributes, stats, and methods for the player character.
*   `enemy.py`: Contains the `Enemy` class, used to create enemy instances with their own stats and XP rewards.
*   `skills.py`: Defines `AVAILABLE_SKILLS`, a list of skills that players can acquire, including their requirements and descriptions.
*   `notifications.py`: Provides the `show_notification()` function for displaying system messages and events in the console.
*   `main.py`: A script that demonstrates the core functionalities by creating a player and an enemy, and simulating a basic combat interaction.
*   `tests/`: This directory contains unit tests for the project.
    *   `test_player.py`: Includes unit tests for the `Player` class to ensure its methods and logic work correctly.
*   `README.md`: This file, providing an overview and documentation for the project.

## Future Work

This project is under active development. Future phases aim to expand on this foundation by adding more features inspired by Solo Leveling, such as:

*   Advanced combat mechanics
*   Diverse skill types (active, passive, buffs, debuffs)
*   Skill effects implementation
*   Player-controlled Shadow Army
*   Daily Quests and Penalties
*   Inventory System
*   Class Evolutions
*   And much more!
