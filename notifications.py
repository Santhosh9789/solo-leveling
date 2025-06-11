def show_notification(message, player_name=None):
    if player_name:
        print(f"[{player_name}'s System]: {message}")
    else:
        print(f"SYSTEM: {message}")

# Example usage (can be removed or commented out):
# show_notification("Level Up!", player_name="Hero")
# show_notification("New Skill Unlocked: Stealth", player_name="Hero")
# show_notification("Enemy Approaching!")
