from skills import AVAILABLE_SKILLS # Import AVAILABLE_SKILLS
from notifications import show_notification # Import notification system
from enemy import Enemy # Import Enemy class

class Player:
    def __init__(self, name="Player"): # Added name for potential future use
        self.name = name
        self.level = 1
        self.experience = 0
        self.stats = {
            "Strength": 10,
            "Agility": 10,
            "Intelligence": 10,
            "Stamina": 10,
            "Perception": 10
        }
        self.skills = []
        self.inventory = []
        self.current_class = "Novice"
        self.shadow_army = []
        self.titles = []
        self.stat_points_to_allocate = 0
        self.experience_to_next_level = 0 # Initial value, will be set by helper
        self.calculate_secondary_stats() # Initial calculation
        self.calculate_experience_to_next_level() # Set initial XP threshold

    def calculate_experience_to_next_level(self): # New helper method
        self.experience_to_next_level = self.level * 100

    def calculate_secondary_stats(self):
        self.hp = self.stats["Stamina"] * 10
        self.mp = self.stats["Intelligence"] * 10

    def increase_stat(self, stat_name, amount):
        if stat_name in self.stats:
            self.stats[stat_name] += amount
            # Recalculate secondary stats if a relevant primary stat changed
            if stat_name == "Stamina" or stat_name == "Intelligence":
                self.calculate_secondary_stats()
            show_notification(f"{stat_name} increased by {amount}. New value: {self.stats[stat_name]}", self.name)
            return True
        else:
            show_notification(f"Error: Invalid stat name '{stat_name}'.", self.name)
            return False

    def gain_experience(self, amount):
        self.experience += amount
        show_notification(f"Gained {amount} XP. Total XP: {self.experience}/{self.experience_to_next_level}", self.name)

        while self.experience >= self.experience_to_next_level: # Use a while loop in case of multiple level ups
            self.level_up()

    def level_up(self):
        # Carry over excess experience
        excess_xp = self.experience - self.experience_to_next_level

        self.level += 1
        self.experience = excess_xp # Assign excess XP as current XP for the new level

        self.calculate_experience_to_next_level() # Update XP needed for the *new* next level

        self.stat_points_to_allocate += 5
        self.calculate_secondary_stats() # Recalculate HP/MP (though base stats didn't change here, good practice)

        show_notification(f"LEVEL UP! You have reached Level {self.level}!", self.name)
        show_notification(f"You have {self.stat_points_to_allocate} stat points to allocate.", self.name)
        self.check_skill_unlocks() # Call this after level up and other operations

    def learn_skill(self, skill_name): # Helper to check if skill already learned by name
        for learned_skill in self.skills:
            # Assuming self.skills stores skill dictionaries
            if isinstance(learned_skill, dict) and learned_skill.get("name") == skill_name:
                return True
        return False

    def check_skill_unlocks(self):
        for skill in AVAILABLE_SKILLS:
            if self.level >= skill["level_requirement"] and not self.learn_skill(skill["name"]):
                self.skills.append(skill) # Store the whole skill dictionary
                show_notification(f"New Skill Unlocked: {skill['name']}!", self.name)

    # Optional: display_skills method
    def display_skills(self):
        if not self.skills:
            show_notification(f"{self.name} has no skills yet.", self.name) # Changed to notification
            return
        # Using print for this multi-line display might be okay, or build a single string for notification
        # For now, let's keep it as print as it's a display method, not a single event.
        # If it needed to be a single notification, the message formatting would be different.
        print(f"\n--- {self.name}'s Skills ---")
        for skill in self.skills:
            print(f"- {skill['name']}: {skill['description']}")
        print("--------------------")

    def attack_enemy(self, enemy_instance): # Placeholder for future combat
        if not enemy_instance.is_alive():
            show_notification(f"{enemy_instance.name} is already defeated.", self.name)
            return

        # Simple attack logic: player's strength vs enemy's HP for now
        damage = self.stats["Strength"]
        show_notification(f"You attack {enemy_instance.name} for {damage} damage!", self.name)
        enemy_instance.take_damage(damage) # This will print enemy's damage status

        if not enemy_instance.is_alive():
            self.defeat_enemy(enemy_instance) # Call defeat_enemy if attack kills

    def defeat_enemy(self, enemy_instance):
        if enemy_instance.is_alive(): # Should not happen if called from attack_enemy correctly
            show_notification(f"Error: {enemy_instance.name} is still alive.", self.name)
            return

        show_notification(f"You have defeated {enemy_instance.name}!", self.name)
        self.gain_experience(enemy_instance.experience_reward)
        # Future: Handle loot, kill counts etc.
