# main.py
from player import Player
from enemy import Enemy
from notifications import show_notification # if you want to use it directly here

if __name__ == "__main__":
    # Setup
    player1 = Player("Hero")
    # Initialize with a more descriptive stats dictionary for Enemy
    goblin = Enemy(name="Goblin", stats={"hp": 30, "attack": 5, "defense": 2}, experience_reward=50, loot_drops=["goblin_ear", "rusty_dagger"])

    show_notification(f"{player1.name} (Level {player1.level}) encounters {goblin.name} (HP: {goblin.current_hp}, XP Reward: {goblin.experience_reward})!", player1.name)
    player1.display_skills() # Show initial skills (should be none or Minor Heal if level 3 by default)

    # Simulate combat
    # Player attacks goblin until it's defeated
    attack_count = 0
    while goblin.is_alive() and player1.hp > 0: # Basic loop, assuming player always hits
        attack_count += 1
        show_notification(f"--- Combat Turn {attack_count} ---", player1.name)
        player1.attack_enemy(goblin)

        # Future: Add enemy attack back, more complex combat logic
        if not goblin.is_alive():
            show_notification(f"{goblin.name} was defeated in {attack_count} attacks.", player1.name)
            break

        # Simple enemy attack back (conceptual placeholder)
        # if goblin.is_alive():
        #     player_damage_taken = goblin.stats.get("attack", 1)
        #     # Assuming player has a take_damage method or direct HP modification
        #     # For now, let's assume Player class will get a take_damage method later
        #     # player1.take_damage(player_damage_taken)
        #     # show_notification(f"{goblin.name} attacks {player1.name} for {player_damage_taken} damage. Player HP: {player1.hp}", player1.name)
        #     # if player1.hp <= 0:
        #         # show_notification(f"{player1.name} has been defeated by {goblin.name}!", player1.name)
        #         # break

        if attack_count > 10: # Safety break for the loop
            show_notification("Safety break: Too many attack turns.", player1.name)
            break

    print("\n--- Player Stats After Combat ---")
    show_notification(f"Level: {player1.level}", player1.name)
    show_notification(f"XP: {player1.experience}/{player1.experience_to_next_level}", player1.name)
    # Assuming max HP is self.stats["Stamina"] * 10, which is updated by calculate_secondary_stats
    show_notification(f"HP: {player1.hp}/{player1.stats['Stamina']*10}", player1.name)
    show_notification(f"Stat Points to Allocate: {player1.stat_points_to_allocate}", player1.name)
    player1.display_skills() # Display skills, which might include newly unlocked ones

    # Example of trying to attack a defeated enemy
    # show_notification("\n--- Attempting to attack defeated enemy ---", player1.name)
    # player1.attack_enemy(goblin) # Should show "already defeated"

    # Example of gaining more XP to potentially level up multiple times
    # show_notification("\n--- Gaining more XP ---", player1.name)
    # player1.gain_experience(250) # Enough for potentially 2 more levels if starting from 0 XP post-goblin
    # show_notification(f"Level: {player1.level}", player1.name)
    # show_notification(f"XP: {player1.experience}/{player1.experience_to_next_level}", player1.name)
    # show_notification(f"Stat Points to Allocate: {player1.stat_points_to_allocate}", player1.name)
    # player1.display_skills()
